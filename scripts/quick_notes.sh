#!/bin/bash

fecha=$(date +"%d-%m-%Y %H:%M:%S")
echo "" >> "$HOME/Documentos/notas_rapidas.md"
konsole -e vim +$ -c "normal G" -c "normal o# $fecha

" "$HOME/Documentos/notas_rapidas.md"