# HUSKY INTEGRATION

## INSTALACION

```
npm install --save-dev husky
```

## CONFIGURACION

```
npx husky init

```

## Solo en linux | mac

```
chmod +x .husky/commit-msg
```

## Configuracion de commit-msg

El archivo commit-msg se encuentra dentro de la carpeta .husky
no debe tener extension para que sea script shell

```
#!/usr/bin/env sh

# Usar el script validator que incluye mensajes de ayuda

node ./commit-validator.js "$1"

```

## Configuracion de pre-commit

```
#!/usr/bin/env sh
# Eliminar la línea . "$(dirname -- "$0")/_/husky.sh" como indica el aviso

# Ejecutar el script JavaScript o simplemente salir con éxito
node -e "console.log('Pre-commit hook ejecutado correctamente'); process.exit(0);"
```
