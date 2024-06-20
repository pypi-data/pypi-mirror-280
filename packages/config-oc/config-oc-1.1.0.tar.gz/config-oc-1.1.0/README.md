# Ouroboros Coding Config
[![pypi version](https://img.shields.io/pypi/v/Config-OC.svg)](https://pypi.org/project/Config-OC) ![MIT License](https://img.shields.io/pypi/l/Config-OC.svg)

A module to simplify documenting and loading configuration files written in JSON with the ability to seperate public from private data.

# Requires
Config-OC requires python 3.10 or higher

## Installation
```bash
pip install Config-OC
```

# Usage

## Creating Files

Using the module does not actually require any files, however it is strongly suggested both are created to get the full benefits of the module. Not doing so will result in an error printed to stderr, but the module will still work as intended, just with no settings.

### Base Settings

The first file is always called config.json. Its purpose is to provide a document detailing all possible settings, as valid types, if not necessarily functional values.

config.json:
```json
{
  "mariadb": {
    "host": "localhost",
    "port": 3306,
    "user": "foobar_user",
    "passwd": "",
    "db": "foobar",
    "charset": "utf8"
  },

  "redis": {
    "host": "localhost",
    "port": 6379,
    "password": "",
    "db": 0
  }
}
```

Notice, we don't put any password in here, these value do not need to work, they just need to provide information to the developer. In this case, that the config.mariadb.password value needs to be a string. This is a safe way to provide documentation, as well as safe default values, that can be stored in source control and shared publicly.

### Host Specific Settings

The second file is named based on the hostname of the machine the script is running on. It allows you to set host specific, or private, settings in a file associated only with the host. It should never be stored in source control, and thus never shared publicly, even accidently.

It also starts with config, and ends in .json but contains the name of the host in the middle. For example, say my development machine was called "chris"

```bash
$: echo `hostname`
chris
```

I would then create my specific settings file as config.chris.json. An easy way to do so from the command line would be using the command used above to generate the filename

```bash
$: touch config.`hostname`.json
$: ls
config.chris.json
```

This file contains only the changes you want to see on top of the base settings. For example, I am still on my development machine, and MariaDB is running locally, on the default port, with the default databases name, and the default database user, with the default charset. Sounds like all I need is to set the password. In fact, same deal for Redis, my default settings are good for all but password. So let's set our config.chris.json

config.chris.json
```json
{
  "mariadb": {
    "passwd": "d7e8fuisdjf02233"
  },

  "redis": {
    "password": "aepof20rif323t23"
  }
}
```

But what if I was not on my development machine, what if I was on a staging server, called "preprod" and both softwares are still local, still on the default port, but using a different db, user, and password?

config.preprod.json
```json
{
  "mariadb": {
    "user": "staging_user",
    "passwd": "g38s5h2k1ng38dby",
    "db": "staging"
  },

  "redis": {
    "password": "4ng8sl26flv3s8hs",
    "db": 1
  }
}
```

And, last example, we're in production, on our thundercougarfalconbird server, and the hosts of both softwares is external, and the passwords are needed, but the rest is fine as is.

config.thundercougarfalconbird.json
```json
{
  "mariadb": {
    "host": "db.somedomain.com",
    "passwd": "4kf8an38d8nf4alf0"
  },

  "redis": {
    "host": "cache.somedomain.com",
    "password": "f8askgwk9shostfd"
  }
}
```

## Using config
So now we have our configuration, but we need access to the data. First, let's
see how we can get all of it.

script.py:
```python
from config import config
from pprint import pprint

pprint(
  config()
)
```

If we we on my dev machine, the output would be something like this

```bash
{'mariadb': {'charset': 'utf8',
             'db': 'foobar',
             'host': 'localhost',
             'passwd': 'd7e8fuisdjf02233',
             'port': 3306,
             'user': 'foobar_user'},
 'redis': {'db': 0,
           'host': 'localhost',
           'password': 'aepof20rif323t23',
           'port': 6379}}
```

If we were on the production server, the output would be something like this

```bash
{'mariadb': {'charset': 'utf8',
             'db': 'foobar',
             'host': 'db.somedomain.com',
             'passwd': '4kf8an38d8nf4alf0',
             'port': 3306,
             'user': 'foobar_user'},
 'redis': {'db': 0,
           'host': 'cache.somedomain.com',
           'password': 'f8askgwk9shostfd',
           'port': 6379}
}
```

But it's not at all necessary to get the entire dictionary of settings, nor is config even a function really. It's simply a shorthand to get a copy of all settings. Nothing stops you from getting just one section (dev)

script.py:
```python
pprint(
  config.mariadb()
)
```

```bash
{'db': 'foobar',
 'host': 'localhost',
 'password': 'd7e8fuisdjf02233',
 'port': 3306,
 'user': 'foobar_user'
}
```

Or even just one value

script.py:
```python
pprint(
  config.mariadb.host()
)
```

```bash
'localhost'
```

So why the function call? Why not just return the data at the level requested and be done with it? Well, because then we couldn't have another level of security by allowing the developer to specify exactly what is necessary, regardless of the settings file. I mean, what if someone forgets a value? Should your code crash because something is missing in a text file? Or maybe, something like a port, is so generic, and so likely to be the default, that you want to allow the opportunity to change it, but you're not advertising it because you want to push people to just stick with the default port? In fact, for Redis, there's a good chance the db and the port are never going to change, let's not bog down the user with these options.

config.json:
```json
{
  "redis": {
    "host": "localhost",
    "password": ""
  }
}
```

config.chris.json:
```json
{
  "redis": {
    "password": "aepof20rif323t23"
  }
}
```

script.py:
```python
from config import config
from pprint import pprint

pprint(
  config.redis({
    'host': 'localhost',
    'port': 6379,
    'password': '',
    'db': 0
  })
)
```

```bash
{'db': 0,
 'host': 'localhost',
 'password': 'aepof20rif323t23',
 'port': 6379
}
```

And there's no reason why you need to access the data immediately, or as an entire section. What if I just want to pull out a part of the data and pass it along before I make any decisions about what defaults it needs, or even what parts I need?

script.py:
```python
from config import config, Data

def print_settings(conf: 'Data') -> None:
  print('All: %s' % str(conf()))
  print('Host: %s' % conf.host('localhost'))
  print('Port: %d' % conf.port(6379))
  print('DB: %d' % conf.db(0))

redis_conf = config.redis
print_settings(redis_conf)
```

```bash
All: {'db': 0, 'host': 'localhost', 'password': 'aepof20rif323t23', 'port': 6379}
Host: localhost
Port: 6379
DB: 0
```

And this works regardless of what you've tried to access or whether it exists or not. As an example, there is no section for logging in our original config, or the host specific ones. Logging is never even mentioned.

script.py:
```python
from config import config, Data

def print_settings(conf: 'Data') -> None:
  print('All: %s' % str(conf()))
  print('Name template: %s' % conf.name_template('file.%d.log'))
  print('Max size: %s' % conf.max_size(10485760))
  print('Max files: %d' % conf.max_files(10))

logging_conf = config.logging
print_settings(logging_conf)
```

```bash
All: None
Name template: file.%d.log
Max size: 10485760
Max files: 10
```

So why did this code work? There's no "logging" in our configuration files, and we didn't add it at runtime, shouldn't this throw a exception? Maybe an AttributeError? Sure, it could have been designed that way, but then you'd always be stuck in a place where you need to decide whether you want to make something configurable or not. Maybe you just want the option, in the future, but again, you're not advertising it to the world. Maybe it's a beta feature, but should you personally have to commit, push, update, test, commit, push, updated, test, again and again to adjust something?

## Reloading

If it's necessary to update the config without restarting your application, you can simply use the `reload()` method. This will re-open both config files and change what is currently in memory.

```python
>>> import config
config-oc.config unable to load config.json
config-oc unable to load config.hostname.json
>>> config()
{}
>>> import strings
>>> strings.to_file('config.json', '{"test": "hello"}')
True
>>> config.reload()
config-oc unable to load config.hostname.json
>>> config()
{'test': 'hello'}
```

Keep in mind that if you have a Data pointer currently in use anywhere in your code you will have to re-fetch it from config else you will be holding onto something that very well doesn't exist in memory anymore.