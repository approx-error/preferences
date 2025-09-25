# Cheatsheet for common commands

## System information checking

### free

Check available memory in human readable form

```sh
free -h
```

### lscpu

Check information about cpu:

```sh
lscpu
```

### lspci

Check information about graphics card / gpu and other PCI-connected devices

```sh
lspci
```

## Archiving and Compressing

### tar

Create tar named archive.tar from directory called directory:

```sh
tar -cf archive.tar directory
```

List all files in archive.tar verbosely:

```sh
tar -tvf archive.tar
```

Extract all files from acrhive.tar:

```sh
tar -xf archive.tar
```

### gzip

Compress file named data.dat and DON'T keep the original:

```sh
gzip data.dat
```

Compress file named data.dat and DO keep the original:

```sh
gzip -k data.dat
```

Decompress file named data.dat.gz:

```sh
gzip -d data.dat
```
