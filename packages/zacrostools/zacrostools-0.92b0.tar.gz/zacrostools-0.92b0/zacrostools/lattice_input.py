from zacrostools.write_functions import write_header


class LatticeModel:
    """A class that represents a lattice model.

    Parameters
    ----------
    lines: list of str
        Lines that will be printed in the lattice_input.dat.
    """

    def __init__(self, lines=None):
        if isinstance(lines, list):
            self.lines = lines
        else:
            print("Error: parameter 'lines' in LatticeModel is not a list")

    @classmethod
    def from_file(cls, path):
        """Create a LatticeModel by reading an existing lattice_input.dat file.

        Parameters
        ----------
        path: str
            Path to the directorey where the lattice_input.dat file is located


        Returns
        -------
        lattice_model: LatticeModel

        """

        lattice_lines = []
        start_pattern_detected = False
        end_pattern_detected = False

        with open(path, 'r') as infile:

            while not start_pattern_detected:
                line = infile.readline()
                if 'default_choice' in line or 'periodic_cell' in line or 'explicit' in line:
                    lattice_lines.append(line)
                    start_pattern_detected = True

            while not end_pattern_detected:
                line = infile.readline()
                if 'end_lattice' in line:
                    lattice_lines.append(line)
                    end_pattern_detected = True
                else:
                    lattice_lines.append(line)

        lattice_model = cls(lines=lattice_lines)
        return lattice_model

    def write_lattice_input(self, path):
        """Write the lattice_input.dat file.

        Parameters
        ----------
        path: str
            Path to the directory where the lattice_input.dat file will be written.

        """
        write_header(f"{path}/lattice_input.dat")
        with open(f"{path}/lattice_input.dat", 'a') as infile:
            for line in self.lines:
                infile.write(line)

    def repeat_cell(self, repeat_cell):
        """Modify the value of the repeat_cell keyword in the lattice_input.dat file.

        Parameters
        ----------
        repeat_cell: list of int, optional
            Updates the repeat_cell keyword in lattice_input.dat file.

        """
        for i, line in enumerate(self.lines):
            if 'repeat_cell' in line:
                self.lines[i] = f'   repeat_cell {repeat_cell[0]} {repeat_cell[1]}\n'
