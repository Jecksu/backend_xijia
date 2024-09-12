

from nii_procesor.processor import processor
from NiiProcessorArgParser import NiiProcessorArgParser


def main(input, output_path, operation_list):

    p = processor()
    p.read_nii(input)
    for operation in operation_list:
        for op, args in operation.items():
            getattr(p, op)(**args)
        print(f"Operation {op} with args {args} done")

    p.write_nii(output_path)


if __name__ == "__main__":
    parser=NiiProcessorArgParser()

    # get input, output path and operation list
    input_path = parser.get_input_path()
    output_path = parser.get_output_path()
    operation_list = parser.get_operationlist()
   
    main(input_path, output_path, operation_list)
