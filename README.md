# Moodle Scraper
A scraper for older versions of Moodle.

- Instead of using outdated packages in older version. I am going to use webkit to get a screen capture of the page to retain the nice formatting.
  - currently looking at packages:
    1. `PyQt`
    2. `PySide`
    3. `Ghost`
  - These packages don't really support login right now. Might have to find a work around.
- [Probably low priority] And A pdf file will be created containing all the screenshots of a course.
- Investigate structure of older versions of moodle to get the files `.doc . pdf etc`
- Replace redirect links with actual target.


### Log

#### 11/27

Reading thru the old scraper and investigate on better libs to use. Found `PyQt` , `PySide` and `Ghost`

#### 11/28

Installing moodle on Mac with mama and stuffs. However, `macOS sierra` has incompatibility with `PyQt` or `PySide` packages which are essential for `screen capture` of particular page.

Found a bash tool that works quite well on taking a screen capture. However, needs to deal with login.

Sample Capture results are saved to `webkit2png outputs` folder.

#### 11/29

Trying to restore moodle site with the test data given by Andrew. Failed a few attempts. Trying to reset back. However, now it just hangs on `checking environments`.

Still stuck on  `checking environments` after 5 attempts by following installation guide for version `1.9 2.0 2.1 2.2 2.3 2.4 2.5`

#### 11/30

After various tries with stuffs, settle down to use a combination of `Firefox` and `selenium` to capture the page. Right now it is working however it captures before the page fully loaded for some reason.

Update:

A dummy wait is implemented in this case. It's dumb but it works :)

#### 12/1 ~ 12/5

df
Something awkward… Chrome and Firefox coredrive didn't capture the whole page.

PhantomJS does but there is something weird with the `send_key` function using PhantomJS. Researching reveals the problem lies in some compatibility issue in PhantomJS. People saying falling back to 1.9.8 should work and the creator says it will be fixed in the next patch.

Safari Driver works at first..then auto fails somehow… probably some security stuff going on with it..

#### 12/6

Trying to fix problems found on 12/5. No luck yet.

#### 12/7

Created the moodle server both locally with `mamp` and on a ubuntu vps. Spend a lot of time fixing a issue with php version. Eventually fixed but have to know how to restore the test site with test data provided by andrew.

#### 12/8

Still fixing the issues spotted on 12/5. Found a working solution but it's in `Ruby`. Might have to learn ruby to fix this…

Trying to learn how to administrate moodle as well, but still have to deal with the backup restoring issue.

> And the key.txt is removed for security.

### Comments from Jon:
I would recommend trying to switch to Firefox if you are still having issues with the Chrome JS. You are right that there is an issue with the selenium tool there. I think you are on the right track so far though with resizing the window and then taking a screenshot of it. 
