# Autoblobs

Automatically save and store SHSH blobs for your iOS device in your Telegram.

## Configuration

To configure autoblobs open `config.json`:

```json
{
  "telegram": {
    "bot_token": "0000000000:xxxxxxxxxxxx_xxxxxxxxxxxxxxxxxxxxx",
    "chat_id": "000000000",
    "disable_notification": false
  },
  "device": {
    "identifier": "iPhoneX,X",
    "ecid": "XXXXXXXXXXXXXX"
  },
  "storage_path": "blobs/"
}
```

Fill in your own values and save it.

## Usage

To setup virtual environment use Poetry:

```bash
$ poetry install
```

To start endless loop:

```bash
$ poetry run python main.py
```
