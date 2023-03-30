#!/bin/bash
# ejecutar 
# sudo ln -s $HOME/git_repos/dotfiles/scripts/create_file.sh /usr/local/bin/fc
# para poder ejecutar el comando desde donde quiera, incluso con rofi

# Establece los valores por defecto
filename=""
filetypMarkDowne=".md"
editor='phpstorm'
rutaRedmine="$HOME/Documentos/redmine_doc/"
rutaDocumentos="$HOME/Documentos/"

# Analiza los argumentos de la línea de comandos
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    -r|--rm)
      filename="RM${2:-}.md"
      ruta=$rutaRedmine
      shift # salta el argumento del flag
      ;;
    -t|--type)
      filetype=".$2"
      shift # salta el argumento del flag
      ruta=$rutaDocumentos
      ;;
    *)
      filename="$key"
      ;;
  esac
  shift # salta el argumento procesado
done

# Verifica si se ha proporcionado un nombre de archivo
if [ -z "$filename" ]; then
  echo "Debe proporcionar un nombre de archivo."
  exit 1
fi

# Forma el nombre completo del archivo
filename="$filename$filetypeMarkDown"

# Verifica si el archivo ya existe
if [ ! -f "$ruta$filename" ]; then
  # Si no existe, lo crea
  touch "$ruta$filename"
  echo "Archivo $filename creado."
else
  # Si ya existe, muestra un mensaje
  echo "El archivo $filename ya existe."
fi

$editor $ruta$filename
