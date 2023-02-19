from pathlib import Path

from .InputData import InputData


class Reproc_Input(InputData):
    # pylint: disable=unused-argument
    def __init__(self, input_data_path=None, process_name="Reproc", CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / "Data/Reprocessing_Input.csv"

        # Initialize the superclass
        super().__init__(self.input_data_path, process_name, eval_parameter=True)
