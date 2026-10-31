from pathlib import Path

def inspect_path(path):
    path_obj = Path(path)
    return{
        "exists":path_obj.exists(),
        "is_file":path_obj.is_file(),
        "is_dir":path_obj.is_dir(),
        "name":path_obj.name,
        "suffix":path_obj.suffix,
        "parent":path_obj.parent
    }

def find_files(directory, suffix):
    data = Path(directory)
    result = []
    for item in data.iterdir():
        if item.is_file():
            if item.suffix == suffix:
                result.append(item.name)
    return result

def create_project_dirs(base_dir):
    path = Path(base_dir)
    dir_names = ["config", "data", "logs", "output"]
    for dir in dir_names:
        datadir = path / dir
        datadir.mkdir(parents=True, exist_ok=True)


create_project_dirs("project")
create_project_dirs("project")