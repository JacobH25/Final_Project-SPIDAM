# Changelog

## 2024-04-20
- Initial commit.
- Added code to open File Explorer for uploading.
- Added documentation to upload_file.

## 2024-04-22
- Created clean_data file and edited upload_file to work with clean_data to reformat mp3 to wav, remove metadata, and handle multi-channel.

## 2024-04-23
- Made some small corrections to upload_file. remove_metadata was called twice instead of calling handle_multi_chan function, so I fixed that.
- Removed print statement for checking code.

## 2024-04-24
- Optimized functionality of clean_data.py.
- Reworked the conditional statement in remove_metadata function in clean_data.py and touched up on some documentation in the code.
- Removed print statement at the end of upload_file.py to check that the file was created and returned properly.

## 2024-04-25
- Patched and corrected data_cal.py file. The file now displays all plots properly.
- Data file is complete and ready to tie in with GUI file.
- Added Megan's GUI file to the branch and optimized functionality of other files to work with GUI.

## 2024-04-26
- Merged pull request #1 from JacobH25/testing
  - Tied in Megan's GUI file to work with Janmesh's calculation file (data_cal.py).
  - Functions to act as commands for buttons have been added and implemented to the GUI's buttons.
  - Application is now fully functional.
- Optimized functionality of GUI so the program window is opened first rather than the initial file being uploaded first.
- Merged branch 'master' into 'testjan' (Merge commit)
  - Added README, toml, and requirements.

