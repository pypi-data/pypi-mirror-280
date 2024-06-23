import shutil
from pathlib import Path
from sklearn.model_selection import train_test_split


def folder_train_test_split(source_dir, output_dir, test_size=0.3, random_state=42, extensions=["jpg", "png"], ignore_class=[], copy_source_images=False):
    source_dir = Path(source_dir)
    output_dir = Path(output_dir)

    if isinstance(ignore_class, str):
        ignore_class = [ignore_class]

    shutil_op = shutil.copy if copy_source_images else shutil.move
    for folder in source_dir.iterdir():
        class_name = folder.name
        if folder.is_dir() and (class_name not in ignore_class):
            (output_dir / "train" / class_name).mkdir(parents=True, exist_ok=True)
            (output_dir / "val" / class_name).mkdir(parents=True, exist_ok=True)

            # Dataset Splitting
            files = sorted(path for ext in extensions for path in folder.glob(f"*.{ext}"))
            train_files, test_files = train_test_split(files, test_size=test_size, random_state=random_state)

            # Copy files
            for file in train_files:
                shutil_op(file, output_dir / "train" / class_name / file.name)

            for file in test_files:
                shutil_op(file, output_dir / "val" / class_name / file.name)

            print(f"Class: {class_name} | {len(files)} files found | {len(train_files)} train | {len(test_files)} test")


def folder_train_val_test_split(source_dir, output_dir=None, val_size=0.1, test_size=0.1, random_state=42, extensions=["jpg", "png"], ignore_class=[], copy_source_images=False):
    if output_dir is None:
        output_dir = source_dir

    source_dir = Path(source_dir)
    output_dir = Path(output_dir)

    val_test_size = val_size + test_size
    shutil_op = shutil.copy if copy_source_images else shutil.move
    for folder in source_dir.iterdir():
        class_name = folder.name
        if folder.is_dir() and (class_name not in ignore_class):
            (output_dir / "train" / class_name).mkdir(parents=True, exist_ok=True)
            (output_dir / "val" / class_name).mkdir(parents=True, exist_ok=True)
            (output_dir / "test" / class_name).mkdir(parents=True, exist_ok=True)

            # Dataset Splitting
            files = sorted(path for ext in extensions for path in folder.glob(f"*.{ext}"))
            train_files, test_files = train_test_split(files, test_size=val_test_size, random_state=random_state)
            val_files, test_files = train_test_split(test_files, test_size=test_size / val_test_size, random_state=random_state)

            # Copy files
            for file in train_files:
                shutil_op(file, output_dir / "train" / class_name / file.name)

            for file in val_files:
                shutil_op(file, output_dir / "val" / class_name / file.name)                

            for file in test_files:
                shutil_op(file, output_dir / "test" / class_name / file.name)

            print(f"Class: {class_name} | {len(files)} files found | {len(train_files)} train | {len(val_files)} val | {len(test_files)} test")


def yolo_folder_train_test_split(source_dir, output_dir, test_size=0.3, random_state=42, image_extensions=["jpg", "png"], label_extension="txt", image_folder="images", label_folder="labels", background_folder="background", copy_source_images=False):
    folder_train_test_split(source_dir, output_dir, test_size=test_size, random_state=random_state, extensions=[*image_extensions, label_extension], ignore_class=[background_folder], copy_source_images=copy_source_images)
    folder_train_test_split(source_dir, output_dir, test_size=test_size, random_state=random_state, extensions=image_extensions, ignore_class=[image_folder, label_folder], copy_source_images=copy_source_images)
    
    # Move all background to images folder
    for phase in ["train", "val"]:
        folder = Path(f"{output_dir}/{phase}/background")
        for ext in image_extensions:
            for file in folder.glob(f"*.{ext}"):
                shutil.move(file, f"{output_dir}/{phase}/images/{file.name}")
        shutil.rmtree(folder)
