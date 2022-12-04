### OCR Bot [@Image_To_Text_OCR_Bot](https://t.me/Image_To_Text_OCR_Bot)

> A star ⭐ from you means a lot to us!

<p align="center"><a href="https://www.github.com/StarkBotsIndustries/OCRBot"><img src="https://telegra.ph/file/243d5cb02e7aa0384358f.jpg" width="5000"></a></p>

Telegram bot to extract text from image

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Usage

### Deploy to Heroku
<details>
<summary>Steps to deploy</summary>


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/StarkBotsIndustries/OCRBot)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN`.
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!
</details>

### Local Deploying
<details>
<summary>Steps to deploy</summary>

1. Clone the repo
   ```console
   git clone https://github.com/StarkBotsIndustries/OCRBot
   ```

2. Now head to [this page](https://github.com/UB-Mannheim/tesseract/wiki) and install Tesseract installer. 
   
3. Use it to  install Tesseract and copy the PATH to where it is installed. 

4. Now uncomment out [this line](https://github.com/StarkBotsIndustries/OCRBot/blob/master/OCRBot/ocr.py#L8). Fill the inverted commas with your own PATH.
   
5. Edit `Config.py` and fill the needed variables

6. Enter the directory
   ```console
   cd OCRBot
   ```
  
7. Install all requirements using pip.
   ```console
   pip3 install -r requirements.txt
   ```

8. Run the file
   ```console
   python3 main.py
   ```
</details>

### Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)

## Functions

> More features soon, this is a minimal example :)

1) Extract text from image
2) Send any amount of images at once, and it will work the same.

## To-Do

> That's on you mainly...

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Credits

- [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library

## Support

Channel :- [@StarkBots](https://t.me/StarkBots)

Group Chat :- [@StarkBotsChat](https://t.me/StarkBotsChat)

## :)

[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/StarkBotsIndustries)

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/StarkBotsIndustries)
