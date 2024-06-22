import unittest
from unittest.mock import MagicMock
from performance_evaluation_tool import *

class TestPerformanceEvaluation(unittest.TestCase):
    def setUp(self):
        # 100x100 image with 75% of the pixels being blue from left and 25% being red from right
        self.image1 = cv2.imread("test_image_folder/test1/image.png")

        # 100x100 image with 40% of the pixels being red from left and 60% being blue from right
        self.image2 = cv2.imread("test_image_folder/test2/image.png")

        # 100x100 image with 65% of the pixels being blue from left, 10% of the pixels being black in the middle and 25% being red from right
        self.image3 = cv2.imread("test_image_folder/test3/image.png")

        # 100x100 image with 100% of the pixels being green
        self.image4 = cv2.imread("test_image_folder/test4/image.png")

        self.image1_base_dpath = "test_image_folder/test1"
        self.image2_base_dpath = "test_image_folder/test2"
        self.image3_base_dpath = "test_image_folder/test3"
        self.image4_base_dpath = "test_image_folder/test4"

        self.image1_key = ImageKey("test_image_folder/test1/image.png", self.image1_base_dpath)
        self.image2_key = ImageKey("test_image_folder/test2/image.png", self.image2_base_dpath)
        self.image3_key = ImageKey("test_image_folder/test3/image.png", self.image3_base_dpath)
        self.image4_key = ImageKey("test_image_folder/test4/image.png", self.image4_base_dpath)

        self.image1_instance = ImageInstance(self.image1_key, self.image1_base_dpath)
        self.image2_instance = ImageInstance(self.image2_key, self.image2_base_dpath)
        self.image3_instance = ImageInstance(self.image3_key, self.image3_base_dpath)
        self.image4_instance = ImageInstance(self.image4_key, self.image4_base_dpath)
        
    def test_ImageKey(self):
        image_fpath = "/path/to/image.jpg"
        base_dpath = "/path/to/"
        image_key = ImageKey(image_fpath, base_dpath)

        self.assertEqual(Path(repr(image_key)), Path("image.jpg"))

    def test_ImageInstance(self):
        eval_key = MagicMock()
        eval_key.get_rel_fpath.return_value = "image.jpg"
        basepath = "/path/to/base"
        image_instance = ImageInstance(eval_key, basepath)

        image_instance.load = MagicMock(return_value="image_data")
        self.assertEqual(image_instance.load(), "image_data")

    def test_SemanticSegmentationMatchCalculator(self):
        match_calculator = SemanticSegmentationMatchCalculator(to_ignore=False, ignore_pixels=[])
        matches = match_calculator.match(self.image1_instance, self.image2_instance)
        accumulated = {}
        per_image_matches = {}
        accumulated = dict_matches_adder(accumulated, matches)
        per_image_matches = dict_matches_appender(per_image_matches, matches, self.image1_key)
        output_filename = "metrics.csv"

        self.assertIsInstance(matches, dict)
        self.assertIn("overall", matches)

        summarizer = SummarizeMetrics()
        # Call the summarize method
        summarizer.summarize(accumulated, per_image_matches, output_filename)

        self.assertEqual(summarizer._metrics[(255, 0, 0)]["precision"], 0.4666666666666667)
        self.assertEqual(summarizer._metrics[(255, 0, 0)]["recall"], 0.5833333333333334)
        self.assertEqual(summarizer._metrics[(255, 0, 0)]["iou"], 0.35)
        self.assertEqual(summarizer._metrics[(0, 0, 255)]["precision"], 0.0)
        self.assertEqual(summarizer._metrics[(0, 0, 255)]["recall"], 0.0)
        self.assertEqual(summarizer._metrics[(0, 0, 255)]["iou"], 0.0)

        self.assertEqual(summarizer._metrics['overall']["precision"], 0.35)
        self.assertEqual(summarizer._metrics['overall']["recall"], 0.35)
        self.assertEqual(summarizer._metrics['overall']["iou"], 0.21212121212121213)

    def test_IgnoreBlackPixels(self):
        match_calculator = SemanticSegmentationMatchCalculator(to_ignore=True, ignore_pixels=[0,0,0])
        matches = match_calculator.match(self.image3_instance, self.image2_instance)
        accumulated = {}
        per_image_matches = {}
        accumulated = dict_matches_adder(accumulated, matches)
        per_image_matches = dict_matches_appender(per_image_matches, matches, self.image1_key)
        output_filename = "metrics.csv"

        self.assertIsInstance(matches, dict)
        self.assertIn("overall", matches)

        summarizer = SummarizeMetrics()
        # Call the summarize method
        summarizer.summarize(accumulated, per_image_matches, output_filename)

        self.assertEqual(summarizer._metrics[(255, 0, 0)]["precision"], 0.38461538461538464)
        self.assertEqual(summarizer._metrics[(255, 0, 0)]["recall"], 0.5)
        self.assertEqual(summarizer._metrics[(255, 0, 0)]["iou"], 0.2777777777777778)
        self.assertEqual(summarizer._metrics[(0, 0, 255)]["precision"], 0.0)
        self.assertEqual(summarizer._metrics[(0, 0, 255)]["recall"], 0.0)
        self.assertEqual(summarizer._metrics[(0, 0, 255)]["iou"], 0.0)

        self.assertEqual(summarizer._metrics['overall']["precision"], 0.2777777777777778)
        self.assertEqual(summarizer._metrics['overall']["recall"], 0.2777777777777778)
        self.assertEqual(summarizer._metrics['overall']["iou"], 0.16129032258064516)

    def test_precision_recall_positive(self):
        # Create instance of SummarizeMetrics
        summarizer = SummarizeMetrics()

        match_calculator = SemanticSegmentationMatchCalculator(to_ignore=False, ignore_pixels=[])
        matches = match_calculator.match(self.image1_instance, self.image1_instance)
        accumulated = {}
        per_image_matches = {}
        accumulated = dict_matches_adder(accumulated, matches)
        per_image_matches = dict_matches_appender(per_image_matches, matches, self.image1_key)
        output_filename = "metrics.csv"

        # Call the summarize method
        summarizer.summarize(accumulated, per_image_matches, output_filename)

        for cls in summarizer._metrics:
            self.assertEqual(summarizer._metrics[cls]["precision"], 1.0)
            self.assertEqual(summarizer._metrics[cls]["recall"], 1.0)

        for key, value in summarizer._per_image_metrics.items():
            for k,v in value.items():
                if k != 'query_image_fpath' and k != 'reference_image_fpath':
                    self.assertEqual(v['precision'], 1.0)
                    self.assertEqual(v["recall"], 1.0)

    def test_precision_recall_negative(self):
        summarizer = SummarizeMetrics()
        match_calculator = SemanticSegmentationMatchCalculator(to_ignore=False, ignore_pixels=[])
        matches = match_calculator.match(self.image1_instance, self.image4_instance)
        accumulated = {}
        per_image_results = {}
        accumulated = dict_matches_adder(accumulated, matches)
        per_image_results = dict_matches_appender(per_image_results, matches, self.image1_key)
        output_filename = "metrics.csv"

        summarizer.summarize(accumulated, per_image_results, output_filename)

        for cls in summarizer._metrics:
            self.assertEqual(summarizer._metrics[cls]["precision"], 0.0)
            self.assertEqual(summarizer._metrics[cls]["recall"], 0.0)

        for key, value in summarizer._per_image_metrics.items():
            for k,v in value.items():
                if k != 'query_image_fpath' and k != 'reference_image_fpath':
                    self.assertEqual(v['precision'], 0.0)
                    self.assertEqual(v["recall"], 0.0)

    def test_disjoint_keysets(self):
        query_base_dpath = "/path/to/query"
        reference_base_dpath = "/path/to/reference"

        query_keys = set([ImageKey(f"{query_base_dpath}/image1.jpg", query_base_dpath), 
                          ImageKey(f"{query_base_dpath}/image2.jpg", query_base_dpath), 
                          ImageKey(f"{query_base_dpath}/image3.jpg", query_base_dpath), 
                          ImageKey(f"{query_base_dpath}/image4.jpg", query_base_dpath), 
                          ImageKey(f"{query_base_dpath}/image5.jpg", query_base_dpath)])

        reference_keys = set([ImageKey(f"{reference_base_dpath}/image6.jpg", reference_base_dpath), 
                              ImageKey(f"{reference_base_dpath}/image7.jpg", reference_base_dpath), 
                              ImageKey(f"{reference_base_dpath}/image8.jpg", reference_base_dpath), 
                              ImageKey(f"{reference_base_dpath}/image9.jpg", reference_base_dpath), 
                              ImageKey(f"{reference_base_dpath}/image10.jpg", reference_base_dpath)])

        evaluation_keys = query_keys.intersection(reference_keys)

        self.assertEqual(len(evaluation_keys), 0)
    
    def test_dict_values_adder(self):
        accumulated = {
            'class_1': {'num_matches': 10, 'num_unmatched_queries': 10, 'num_unmatched_references': 10}, 
            'class_2': {'num_matches': 15, 'num_unmatched_queries': 10, 'num_unmatched_references': 10}, 
            'overall': {'num_matches': 25, 'num_unmatched_queries': 20, 'num_unmatched_references': 20}}
        
        current = {
            'class_1': {'num_matches': 5, 'num_unmatched_queries': 5, 'num_unmatched_references': 5}, 
            'class_2': {'num_matches': 10, 'num_unmatched_queries': 5, 'num_unmatched_references': 5}, 
            'overall': {'num_matches': 15, 'num_unmatched_queries': 10, 'num_unmatched_references': 10}}

        expected_result = {
            'class_1': {'num_matches': 15, 'num_unmatched_queries': 15, 'num_unmatched_references': 15}, 
            'class_2': {'num_matches': 25, 'num_unmatched_queries': 15, 'num_unmatched_references': 15}, 
            'overall': {'num_matches': 40, 'num_unmatched_queries': 30, 'num_unmatched_references': 30}}

        self.assertEqual(dict_matches_adder(accumulated, current), expected_result)

    def test_dict_values_adder_same_keys(self):
        # Test case where both dictionaries have the same keys
        accumulated = {
            'class_1': {'num_matches': 10, 'num_unmatched_queries': 10, 'num_unmatched_references': 10},
            'class_2': {'num_matches': 20, 'num_unmatched_queries': 20, 'num_unmatched_references': 20},
            'overall': {'num_matches': 30, 'num_unmatched_queries': 30, 'num_unmatched_references': 30}}

        current = {
            'class_1': {'num_matches': 5, 'num_unmatched_queries': 5, 'num_unmatched_references': 5},
            'class_2': {'num_matches': 15, 'num_unmatched_queries': 15, 'num_unmatched_references': 15},
            'overall': {'num_matches': 25, 'num_unmatched_queries': 25, 'num_unmatched_references': 25}}

        expected_result = {
            'class_1': {'num_matches': 15, 'num_unmatched_queries': 15, 'num_unmatched_references': 15},
            'class_2': {'num_matches': 35, 'num_unmatched_queries': 35, 'num_unmatched_references': 35},
            'overall': {'num_matches': 55, 'num_unmatched_queries': 55, 'num_unmatched_references': 55}}

        self.assertEqual(dict_matches_adder(accumulated, current), expected_result)

    def test_dict_values_adder_different_keys(self):
        # Test case where dictionaries have different keys
        accumulated = {
            'class_1': {'num_matches': 10, 'num_unmatched_queries': 10, 'num_unmatched_references': 10},
            'class_2': {'num_matches': 20, 'num_unmatched_queries': 20, 'num_unmatched_references': 20},
            'overall': {'num_matches': 30, 'num_unmatched_queries': 30, 'num_unmatched_references': 30}}
        
        current = {
            'class_1': {'num_matches': 5, 'num_unmatched_queries': 5, 'num_unmatched_references': 5},
            'class_3': {'num_matches': 15, 'num_unmatched_queries': 15, 'num_unmatched_references': 15},
            'overall': {'num_matches': 25, 'num_unmatched_queries': 25, 'num_unmatched_references': 25}}

        expected_result = {
            'class_1': {'num_matches': 15, 'num_unmatched_queries': 15, 'num_unmatched_references': 15},
            'class_2': {'num_matches': 20, 'num_unmatched_queries': 20, 'num_unmatched_references': 20},
            'class_3': {'num_matches': 15, 'num_unmatched_queries': 15, 'num_unmatched_references': 15},
            'overall': {'num_matches': 55, 'num_unmatched_queries': 55, 'num_unmatched_references': 55}}

        self.assertEqual(dict_matches_adder(accumulated, current), expected_result)

if __name__ == "__main__":
    unittest.main()