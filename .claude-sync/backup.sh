#!/bin/bash
# Faz backup das conversas do Claude para o repositório

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONVERSATIONS_DIR="$REPO_DIR/.claude-sync/conversations"
SOURCE_DIR="$HOME/.claude/projects"

mkdir -p "$CONVERSATIONS_DIR"

echo "Copiando conversas de $SOURCE_DIR..."
cp -r "$SOURCE_DIR"/. "$CONVERSATIONS_DIR/"

echo "Adicionando ao git..."
cd "$REPO_DIR"
git add .claude-sync/conversations/
git commit -m "sync: backup conversas Claude $(date '+%Y-%m-%d %H:%M')"
git push origin $(git branch --show-current)

echo "Backup concluído!"
