import unittest


PRESETS = {
    "2.39:1": 2.39,
    "2.35:1": 2.35,
    "1.85:1": 1.85,
    "1.43:1": 1.43,
    "16:9": 16 / 9,
    "4:3": 4 / 3,
    "1:1": 1.0,
    "9:16": 9 / 16,
    "4:5": 4 / 5,
}


def target_mask(width, height, pixel_aspect, target):
    dar = (width * pixel_aspect) / height
    if dar >= target:
        return target / dar, 1.0
    return 1.0, dar / target


def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def pan_crop(width, height, pan_x, pan_y, zoom):
    crop_width = width / zoom
    crop_height = height / zoom
    allowed_x = max(0.0, (width - crop_width) / 2)
    allowed_y = max(0.0, (height - crop_height) / 2)
    pan_x = clamp(pan_x, -1.0, 1.0)
    pan_y = clamp(pan_y, -1.0, 1.0)
    left = clamp((width - crop_width) / 2 - pan_x * allowed_x, 0.0, width - crop_width)
    top = clamp((height - crop_height) / 2 - pan_y * allowed_y, 0.0, height - crop_height)
    return left, top, left + crop_width, top + crop_height


class GeometryTests(unittest.TestCase):
    def test_square_pixel_masks(self):
        cases = [
            (1920, 1080, 16 / 9),
            (1920, 1080, 2.39),
            (1080, 1920, 9 / 16),
            (1080, 1920, 1.0),
        ]
        for width, height, target in cases:
            mask_width, mask_height = target_mask(width, height, 1.0, target)
            self.assertGreater(mask_width, 0)
            self.assertGreater(mask_height, 0)
            self.assertLessEqual(mask_width, 1.0)
            self.assertLessEqual(mask_height, 1.0)

    def test_non_square_pixel_aspect(self):
        mask_width, mask_height = target_mask(720, 486, 8 / 9, 4 / 3)
        dar = (720 * (8 / 9)) / 486
        self.assertAlmostEqual(dar, 1.3168724279835392)
        self.assertEqual(mask_width, 1.0)
        self.assertAlmostEqual(mask_height, dar / (4 / 3))

    def test_vertical_mask_for_vertical_source(self):
        mask_width, mask_height = target_mask(1080, 1920, 1.0, 16 / 9)
        self.assertAlmostEqual(mask_width, 1.0)
        self.assertAlmostEqual(mask_height, (1080 / 1920) / (16 / 9))

    def test_pan_crop_bounds(self):
        bounds = pan_crop(1920, 1080, 1.0, -1.0, 2.0)
        left, top, right, bottom = bounds
        self.assertGreaterEqual(left, 0)
        self.assertGreaterEqual(top, 0)
        self.assertLessEqual(right, 1920)
        self.assertLessEqual(bottom, 1080)

    def test_pan_axis_is_clamped(self):
        bounds = pan_crop(1920, 1080, 10.0, -10.0, 4.0)
        left, top, right, bottom = bounds
        self.assertGreaterEqual(left, 0)
        self.assertGreaterEqual(top, 0)
        self.assertLessEqual(right, 1920)
        self.assertLessEqual(bottom, 1080)

    def test_preset_targets_are_in_range(self):
        for target in PRESETS.values():
            self.assertGreaterEqual(target, 0.50)
            self.assertLessEqual(target, 4.00)


if __name__ == "__main__":
    unittest.main()
