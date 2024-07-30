from pathlib import Path

class FileSystemEntity:
    """
    A class to represent a file system entity (file or directory).

    Attributes
    ----------
    path : Path
        The path to the file or directory.
    name : str
        The name of the file or directory.
    parent : Path
        The parent directory of the file or directory.
    type : str
        The type of the entity ('File', 'Directory', or 'Unknown').

    Methods
    -------
    is_dir():
        Checks if the entity is a directory.
    is_file():
        Checks if the entity is a file.
    """

    def __init__(self, path):
        """
        Initializes the FileSystemEntity with the given path and parent directory.

        Parameters
        ----------
        path : str or Path
            The path to the file or directory.
        """
        if type(path) == str: path = Path(path)
        self.path = path
        self.name = path.name
        self.type = self._get_type()
    
    def _get_type(self):
        """
        Determines the type of the file system entity.

        Returns
        -------
        str
            'Directory' if the entity is a directory, 'File' if it is a file, otherwise 'Unknown'.
        """
        if self.path.is_dir():
            return 'Directory'
        elif self.path.is_file():
            return 'File'
        else:
            return 'Unknown'


