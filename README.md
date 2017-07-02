Browse Indico from the command line by downloading all material from a list
of categories.

# NAME

indicolite – Browse Indico from the command line

# SYNOPSIS

See **indicolite -h**.

# DESCRIPTION

Download all material from a list of categories.

# CONFIGURATION FILE

Indicolite mostly operates from a configuration files which looks like this:

```
server: 'https://indico.yoursite.net'
secret: '00000000-0000-0000-0000-000000000000'
token: '11111111-1111-1111-1111-111111111111'

downloads: 'path/to/directory'
since: '18 April 2016'
categories:
    foo: 1111
    bar: 2222
    baz: 3333
    boo: 4444
warnexist: true
```
