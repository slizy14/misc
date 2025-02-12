# leisen

## Basis Konfiguration
```shell
git config --global user.name "Stefan Leisenberger"
git config --global user.email "stefan.leisenberger@fhj.com"
```

## git clone
Als erstes muss das Repository heruntergeladen werden.
```shell
git clone
```
Je nachdem welches Repository angesprochen wird, muss man sich authentifizieren.

## git status
Mit diesem Kommando kann ma sich den aktuellen Status des Repositories ansehen. 
```shell
git status
```

## git add
Die Änderungen einer Datei zum nächsten COMMIT hinzufügen. 
```shell
git add <Datei.txt>
```

## git commit
Eine Datei ins lokale Repository einchecken. Alle Dateien die mit ADD hinzugefügt wurden, werden eingecheckt.
```shell
git commit -m "Commit Nachricht"
```

## git push
Das lokale Repository ins Online-Repository einchecken.
```shell
git push
```

## git log
Die Commit-History ausgeben. Mit --oneline kann man eine komprimierte Dastellung ausgeben.
```shell
git log [--oneline]
```

## ignore
Dateien die nicht eingecheckt werden sollen müssen in der Datei **.gitignore** definiert werden.

## git checkout
Um eine alte Version zu laden, muss dieses Kommando verwendet werden.
```shell
git checkout 3c47ff9
```
Um wieder zur aktuellsten Version zu kommen, muss man folgendes Kommando verwenden.
```shell
git checkout main
```
