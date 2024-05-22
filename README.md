# Status do Projeto: Este projeto está desatualizado e não está mais sendo mantido.



- **Este projeto é um script em Python para automatizar o processo de login e abertura do jogo League of Legends. Utilizando as bibliotecas `pyautogui`, `wmi`, `subprocess`, `BeautifulSoup` e `requests`, o script realiza várias ações, desde verificar se o cliente do jogo está aberto até preencher automaticamente as credenciais de login.**

## Funcionalidades

- **Verificação de Processo**: O script verifica se o processo do cliente do Riot está em execução. Se não estiver, ele inicia o cliente automaticamente.
- **Login Automático**: O script identifica os campos de login e senha na tela e preenche automaticamente com as credenciais fornecidas.
- **Abertura do Jogo**: Após o login, o script navega pelo cliente do jogo e inicia o League of Legends.
- **Consulta de Informações de Conta**: Utilizando requests para acessar o site op.gg, o script obtém e exibe o nível e o elo de várias contas.
- **Interface de Seleção de Conta**: O usuário pode selecionar uma conta de uma lista para efetuar o login, com informações atualizadas sobre cada conta.
