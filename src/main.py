import subprocess


def testar_instalacao():
    print('🚀 Iniciando Teste de Sanidade do pacote Kubesure (PyPI)...\n')
    print('-' * 40)

    # TESTE 2: Como CLI (Linha de comando)
    print("💻 Executando comando de terminal 'kubesure --help':\n")
    try:
        # Finge que o usuário digitou isso no terminal
        resultado = subprocess.run(
            ['kubesure', '--help'],
            capture_output=True,
            text=True,
            check=False,
        )

        if resultado.returncode == 0:
            print(resultado.stdout)
            print('✅ [CLI]: Comando executado com sucesso!')
        else:
            print('⚠️ [CLI]: O comando retornou um erro.')
            print(resultado.stderr)

    except FileNotFoundError:
        print("❌ [CLI]: O comando 'kubesure' não foi encontrado no sistema.")
        print(
            '💡 Nota: Isso é normal se a versão que você publicou no PyPI ainda'
            ' não tinha o [project.scripts] configurado no toml original.'
        )


if __name__ == '__main__':
    testar_instalacao()
