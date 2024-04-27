# Changelog

## 2024-04-27
- Added functionalities to display max resonance frequency in Hz.
- Updated requirements file.
- Merged pull request #5 from JacobH25/testing.
- Updated Requirements File.
- Merged pull request #4 from JacobH25/testing.
- Additional changes for displaying max res frequency.

## 2024-04-26
- Merged branch 'master' into 'testjan' (Merge commit).
- Added README, toml, and requirements.
- Optimized functionality of GUI so the program window is opened first rather than the initial file being uploaded first.
- Merged pull request #1 from JacobH25/testing.
- Tied in Megan's GUI file to work with Janmesh's calculation file (data_cal.py).
- Functions to act as commands for buttons have been added and implemented to the GUI's buttons.
- Application is now fully functional.

## 2024-04-25
- Added Megan's GUI file to the branch and optimized functionality of other files to work with GUI.
- Data file is complete and ready to tie in with GUI file.
- Patched and corrected data_cal.py file. The file now displays all plots properly.

## 2024-04-24
- Removed print statement at the end of upload_file.py to check that the file was created and returned properly.
- Reworked the conditional statement in remove_metadata function in clean_data.py and touched up on some documentation in the code.
- Optimized functionality of clean_data.py.

## 2024-04-23
- Made some small corrections to upload_file. remove_metadata was called twice instead of calling handle_multi_chan function, so I fixed that.
- Removed print statement for checking code.

## 2024-04-22
- Created clean_data file and edited upload_file to work with clean_data to reformat mp3 to wav, remove metadata, and handle multi-channel.

## 2024-04-20
- Added documentation to upload_file.
- Added code to open File Explorer for uploading.
- Initial commit.
