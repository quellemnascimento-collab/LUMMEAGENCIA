#!/bin/bash
# Restaura conversas do repositório para o Claude local

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONVERSATIONS_DIR="$REPO_DIR/.claude-sync/conversations"
DEST_DIR="$HOME/.claude/projects"

if [ ! -d "$CONVERSATIONS_DIR" ]; then
  echo "Nenhuma conversa encontrada no repositório. Rode backup.sh no outro computador primeiro."
  exit 1
fi

echo "Buscando atualizações do repositório..."
cd "$REPO_DIR"
git pull origin $(git branch --show-current)

echo "Restaurando conversas para $DEST_DIR..."
mkdir -p "$DEST_DIR"
cp -rn "$CONVERSATIONS_DIR"/. "$DEST_DIR/"

echo "Restauração concluída! Reinicie o Claude para ver as conversas."
