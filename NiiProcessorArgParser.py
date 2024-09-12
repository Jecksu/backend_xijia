import argparse
import os

operation_args = {
            "resample": ["spacing", "size", "origin", "direction", "method"],
            "blur": ["sigma"],
            "threshold": ["type", "lower", "upper"],
            "rescale": ["min", "max"],
            "denoise": ["min_noise", "max_noise"],
            "edge_detect": ["detect_min", "detect_max"]
        }

class NiiProcessorArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="nii processor")
        self._add_main_arguments()
        self._add_filter_arguments()

    def _add_main_arguments(self):
        self.parser.add_argument("--input", "-i", type=str, help="input nii file path", required=True)
        self.parser.add_argument("--output", "-o", type=str, help="output nii file path", required=True)
        self.parser.add_argument("--filter", type=str, nargs='+', help="filters to apply, eg: blur,resample,threshold,rescale,denoise,edge_detection", required=True)

    def _add_filter_arguments(self):
        self._add_blur_arguments()
        self._add_resample_arguments()
        self._add_threshold_arguments()
        self._add_rescale_arguments()
        self._add_denoise_arguments()
        self._add_edge_detection_arguments()

    def _add_blur_arguments(self):
        blur_group = self.parser.add_argument_group("blur", "blur parameters")
        blur_group.add_argument("--sigma", type=float, default=1.5, help="gaussian sigma")

    def _add_resample_arguments(self):
        resample_group = self.parser.add_argument_group("resample", "resample parameters")
        resample_group.add_argument("--spacing", type=float, nargs="+", help="resampling spacing")
        resample_group.add_argument("--size", type=float, nargs="+", help="resampling size")
        resample_group.add_argument("--method", type=str, default="linear", help="resampling method, default linear, options: linear, nearest")
        resample_group.add_argument("--origin", type=float, nargs="+", help="resampling origin")
        resample_group.add_argument("--direction", type=float, nargs="+", help="resampling direction")

    def _add_threshold_arguments(self):
        threshold_group = self.parser.add_argument_group("threshold", "threshold parameters")
        threshold_group.add_argument("--type", type=str, default="otsu", help="threshold type, default otsu, options: otsu, triangle, mean, maximum")
        threshold_group.add_argument("--lower", type=float, default=0, help="threshold lower, default 0")
        threshold_group.add_argument("--upper", type=float, default=1, help="threshold upper, default 1")

    def _add_rescale_arguments(self):
        rescale_group = self.parser.add_argument_group("rescale", "rescale parameters")
        rescale_group.add_argument("--min", type=float, default=0, help="rescale intensity min, default 0")
        rescale_group.add_argument("--max", type=float, default=1, help="rescale intensity max, default 1")

    def _add_denoise_arguments(self):
        denoise_group = self.parser.add_argument_group("denoise", "denoise parameters")
        denoise_group.add_argument("--min_noise", type=float, default=0, help="denoise new min, default 0")
        denoise_group.add_argument("--max_noise", type=float, default=1, help="denoise new max, default 1")

    def _add_edge_detection_arguments(self):
        edge_detect_group = self.parser.add_argument_group("edge_detect", "edge detection parameters")
        edge_detect_group.add_argument("--detect_min", type=int, help="edge detection min")
        edge_detect_group.add_argument("--detect_max", type=int, help="edge detection max")

    def parse_args(self):
        return self.parser.parse_args()
    
    def get_operationlist(self):
        args = vars(self.parser.parse_args())
        filter_list = args.pop("filter") or []
        if not filter_list:
            return []
        
        operation_list = []
        for filter in filter_list:
            if filter in operation_args:
                op_args = {}
                for param in operation_args[filter]:
                    value = args.pop(f"{param}", None)
                    if value is not None:
                        op_args[param] = value
                operation_list.append({filter: op_args})
        return operation_list
    
    def get_input_path(self):
        
        input_path=vars(self.parser.parse_args())["input"]
        # check if input file exists or not
        # if not, raise FileNotFoundError
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"File {input_path} not found")
        return input_path
    
    def get_output_path(self,clean_existing=True):
        output_path=vars(self.parser.parse_args())["output"]
        if os.path.exists(output_path):
            # delete the file if it exists
            if clean_existing:
                os.remove(output_path)
            else:
                raise FileExistsError(f"File {output_path} already exists")
        return output_path
