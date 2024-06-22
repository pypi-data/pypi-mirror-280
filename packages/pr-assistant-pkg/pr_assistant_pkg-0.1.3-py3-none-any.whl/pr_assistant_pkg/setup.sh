# setup.sh
INSTALL_PATH=$(python3 -m site --user-base)/bin
if [[ ":$PATH:" != *":$INSTALL_PATH:"* ]]; then
    echo "export PATH=\$PATH:$INSTALL_PATH" >> ~/.zshrc
    source ~/.zshrc
fi
echo "Installation path added to PATH. Please restart your terminal."
