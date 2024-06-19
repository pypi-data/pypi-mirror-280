from .txt_implementation_functions import *
from .coco_json_implementation_functions import *


class cvPal:
    def __init__(self):
        self.path = None
        self.data_type = None

    def read_data(self, path=None, data_type=None):
        self.path = path
        self.data_type = data_type

    def merge(self, paths, output_folder_name="output", base_storage_path= None, parental_reference=False):

        """
        Merges data from multiple paths and optionally creates a YAML file.

        Parameters:
        paths (list): A list containing multiple paths to the data.
        roboflow (bool): If True, creates a YAML file with the paths and classes.
        inplace (bool): If True, the operation modifies the data in place.
        parental_reference
        """
        if self.data_type.lower() == "txt":
            # Assuming read_data_txt is defined elsewhere and properly handles the parameters.
            new_output_folder_path, excluded_images = merge_data_txt(self.path, paths, output_folder_name, base_storage_path, parental_reference)
            self.path = new_output_folder_path
            print(f"New Dataset saved at {self.path}")
            return self.path

        elif self.data_type.lower() == "coco_json":
            new_output_folder_path =merge_data_json(self.path, paths, parental_reference)
            self.path = new_output_folder_path




    def delete_label(self,label_to_delete):
        """
        Deletes a certain label from the dataset.

        Parameters:
        label_to_delete (str/int): The label to be deleted.
        """

        if self.data_type.lower() == "txt":
            remove_label_from_txt_dataset(self.path, label_to_delete)

        elif self.data_type.lower() == "coco_json":
            pass

    def count_labels(self):
        """
        Counts the occurrence of each label in the dataset.

        Parameters:
        data (list): The dataset for which to count label occurrences.
        """
        if self.data_type.lower() == "txt":
            return count_labels_in_txt_dataset(self.path)

        elif self.data_type.lower() == "coco_json":
            pass

    def replace_label(self, data, replacement_dict):
        """
        Replaces a label in the dataset based on a dictionary of replacements.

        Parameters:
        data (list): The dataset in which to replace labels.
        replacement_dict (dict): A dictionary with old labels as keys and new labels as values.
        """
        if self.data_type.lower() == "txt":
            replace_labels_in_txt_yaml(self.path, replacement_dict)

        elif self.data_type.lower() == "coco_json":
            pass

    def find_files_with_label(self, label, exclusive=False):
        """
        Finds files that contain a certain label.

        Parameters:

        label (str): The label to find.
        exclusive (bool): If True, finds files that contain only the specified label.
        """
        if self.data_type.lower() == "txt":
            result = find_images_with_label_in_txt_type(self.path, label, exclusive)
            return result

        elif self.data_type.lower() == "coco_json":
            pass

    def report(self):
        """
        Creates a DataFrame that contains columns for image path, label, and label path.

        Parameters:
        image_paths (list): A list of image paths.
        label_paths (list): A list of corresponding label paths.
        """
        if self.data_type.lower() == "txt":
            df_report = report(self.path)
            return df_report

        elif self.data_type.lower() == "coco_json":
            pass
