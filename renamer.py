import argparse, os

class Renamer:
    def __init__(self):
        self.args = self.argument_parser()

        self.failed_counter = 0
        self.successful_counter = 0
        self.no_change_counter = 0

    def argument_parser(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser()

        parser.add_argument('--path', required=True, help="path to your file")

        parser.add_argument('-rt', '--rename-type',
            choices = [
                'replace',

                'remove_start',
                'remove_end',
                'remove_from_to',

                'uppercase',
                'lowercase',

                'set_name',
            ],
            required=True, help="choose rename type.")

        parser.add_argument('--params', required=True, help="parameters for chosen rename type")

        return parser.parse_args()

    def is_valid_filename(self, filename: str) -> bool:
        # Characters not allowed in filenames on most operating systems
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

        for char in invalid_chars:
            if char in filename:
                return False

        return True

    def rename(self, old_name: str, new_name: str):
        if self.is_valid_filename(new_name):
            os.rename(self.args.path + '\\' + old_name, self.args.path + '\\' + new_name)
            if old_name == new_name:
                self.no_change_counter += 1
            else:
                print(f'Changes applied to \033[33m{old_name}\033[0m => \033[32m{new_name}\033[0m')
                self.successful_counter += 1

        else:
            print(f'Changes invalid for \033[31m{old_name}\033[0m')
            self.failed_counter += 1


    def replace(self):
        for file_name in os.listdir(self.args.path):
            new_name = os.path.splitext(file_name)
            new_name = new_name[0].replace(*self.args.params.split(':')) + new_name[1]

            self.rename(file_name, new_name)

    def remove_start(self):
        for file_name in os.listdir(self.args.path):
            new_name = os.path.splitext(file_name)
            new_name = new_name[0][int(self.args.params):] + new_name[1]

            self.rename(file_name, new_name)

    def remove_end(self):
        for file_name in os.listdir(self.args.path):
            new_name = os.path.splitext(file_name)
            new_name = new_name[0][:-int(self.args.params)] + new_name[1]

            self.rename(file_name, new_name)

    def remove_from_to(self):
        for file_name in os.listdir(self.args.path):
            new_name = os.path.splitext(file_name)
            param1, param2 = self.args.params.split(':')
            new_name = new_name[0][:int(param1)-1] + new_name[0][int(param2):] + new_name[1]

            self.rename(file_name, new_name)

    def set_uppercase(self):
        for file_name in os.listdir(self.args.path):
            new_name = os.path.splitext(file_name)
            new_name = new_name[0].upper() + new_name[1]

            self.rename(file_name, new_name)

    def set_lowercase(self):
        for file_name in os.listdir(self.args.path):
            new_name = os.path.splitext(file_name)
            new_name = new_name[0].lower() + new_name[1]

            self.rename(file_name, new_name)

    def set_name(self):
        extensions = dict()
        name, separator = self.args.params.split(':')

        for file_name in sorted(os.listdir(self.args.path)):
            new_name = os.path.splitext(file_name)
            ext = new_name[1]

            extensions.setdefault(ext, 0)
            if extensions[ext] == 0: new_name = name + ext
            else: new_name = name + separator + str(extensions[ext]) + ext
            extensions[ext] += 1

            self.rename(file_name, new_name)

    def run(self):
        if os.path.isdir(self.args.path):

            match self.args.rename_type.lower():
                case 'replace': self.replace()

                case 'remove_start': self.remove_start()
                case 'remove_end': self.remove_end()
                case 'remove_from_to': self.remove_from_to()

                case 'uppercase': self.set_uppercase()
                case 'lowercase': self.set_lowercase()

                case 'set_name': self.set_name()

            print()
            print(f'{self.failed_counter} unsuccessful')
            print(f'{self.successful_counter} successful')
            print(f'{self.no_change_counter} unchanged')

        else: print("The path does not exist or is not a folder.")


if __name__ == '__main__':
    Renamer().run()
