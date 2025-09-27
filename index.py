from flask import Flask, request, Response

app = Flask(__name__)
app.url_map.strict_slashes = False

# ... suas rotas /webhook, etc.

@app.route("/privacy", methods=["GET"])
def privacy():
    html = """
    <!doctype html>
    <html lang="pt-br">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Política de Privacidade | Personalité Cuidados em Saúde</title>
      <style>
        body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; max-width: 920px; margin: 40px auto; padding: 0 16px; line-height: 1.6; color: #222; }
        h1, h2 { line-height: 1.25; }
        small, footer { color: #666; }
        a { color: #0a7; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .box { background: #f7f7f7; border: 1px solid #e5e5e5; padding: 12px 16px; border-radius: 8px; }
      </style>
    </head>
    <body>
      <h1>Política de Privacidade</h1>
      <p><strong>Personalité Cuidados em Saúde</strong> (“nós”) respeita sua privacidade. Esta Política descreve como tratamos dados pessoais no contexto de nossos serviços e do nosso bot de WhatsApp.</p>

      <h2>1. Controlador</h2>
      <p><strong>Razão social / Nome fantasia:</strong> Personalité Cuidados em Saúde<br>
         <strong>Contato do responsável (DPO/Encarregado):</strong> &lt;nome do encarregado&gt; – &lt;contato@personalitesaude.com.br&gt; – &lt;telefone&gt;</p>

      <h2>2. Dados que coletamos</h2>
      <ul>
        <li>Dados de contato (nome, telefone, e-mail) fornecidos por você.</li>
        <li>Conteúdo de mensagens trocadas via WhatsApp Business API (inclui texto e metadados, como horário e IDs técnicos).</li>
        <li>Logs técnicos necessários à operação (endereço IP do servidor, timestamps, status de entrega).</li>
      </ul>

      <h2>3. Finalidades e bases legais</h2>
      <ul>
        <li>Atender e responder suas solicitações e prestar nossos serviços de saúde domiciliar (execução de contrato/medidas pré-contratuais).</li>
        <li>Comunicações administrativas e informações sobre agendamentos, orientações e suporte (interesse legítimo/execução de contrato).</li>
        <li>Cumprimento de obrigações legais e regulatórias aplicáveis à área de saúde.</li>
      </ul>
      <p>Tratamos dados de acordo com a <strong>LGPD (Lei 13.709/2018)</strong>. Quando necessário, solicitaremos seu consentimento específico.</p>

      <h2>4. Compartilhamento</h2>
      <p>Poderemos compartilhar dados com:</p>
      <ul>
        <li><strong>Meta Platforms</strong> (WhatsApp Business API) para viabilizar o canal de mensagens.</li>
        <li>Provedores de hospedagem e infraestrutura (por ex., Render) e ferramentas estritamente necessárias à operação.</li>
        <li>Profissionais de saúde da nossa equipe, quando indispensável para o atendimento.</li>
      </ul>
      <p>Não vendemos seus dados pessoais.</p>

      <h2>5. Transferências internacionais</h2>
      <p>Serviços como WhatsApp/Meta e hospedagem podem envolver servidores no exterior. Adotamos salvaguardas adequadas conforme a LGPD.</p>

      <h2>6. Segurança</h2>
      <p>Aplicamos medidas técnicas e organizacionais para proteger os dados contra acessos não autorizados, perda e alteração. Contudo, nenhum sistema é 100% seguro.</p>

      <h2>7. Retenção</h2>
      <p>Guardamos os dados pelo tempo necessário para as finalidades desta Política, obrigações legais e defesa de direitos. Após esse período, eliminamos ou anonimizamos os dados.</p>

      <h2>8. Seus direitos</h2>
      <p>Nos termos da LGPD, você pode solicitar: confirmação de tratamento, acesso, correção, portabilidade, anonimização/eliminação, informação sobre compartilhamentos e revisão de decisões automatizadas, além de revogar consentimentos quando aplicável. Para exercer, contate: <strong>&lt;contato@personalitesaude.com.br&gt;</strong>.</p>

      <h2>9. Cookies e site</h2>
      <p>Se você navegar em páginas nossas (como esta), poderemos usar cookies estritamente necessários para funcionamento. Não utilizamos cookies para publicidade neste contexto.</p>

      <h2>10. Contato</h2>
      <div class="box">
        <p><strong>E-mail:</strong> &lt;contato@personalitesaude.com.br&gt;<br>
           <strong>Endereço:</strong> &lt;Av Miguel Yunes&gt;<br>
           <strong>Telefone/WhatsApp:</strong> &lt;+55 xx xxxxx-xxxx&gt;</p>
      </div>

      <p><small>Última atualização: 27/09/2025</small></p>

      <hr>
      <p>Solicitações de exclusão de dados: consulte nossa <a href="/data-deletion">Política de Exclusão de Dados</a>.</p>

      <footer><small>© Personalité Cuidados em Saúde. Todos os direitos reservados.</small></footer>
    </body>
    </html>
    """
    return Response(html, status=200, mimetype="text/html")


@app.route("/data-deletion", methods=["GET"])
def data_deletion():
    html = """
    <!doctype html>
    <html lang="pt-br">
    <head><meta charset="utf-8"><title>Exclusão de Dados</title></head>
    <body style="font-family: Arial, sans-serif; max-width: 920px; margin: 40px auto; padding: 0 16px;">
      <h1>Política de Exclusão de Dados</h1>
      <p>Para solicitar a exclusão dos seus dados pessoais, envie um e-mail para <strong>&lt;contato@personalitesaude.com.br&gt;</strong>
         com o assunto <em>“Exclusão de dados – WhatsApp”</em> e informe seu nome completo e número de telefone usado na conversa.</p>
      <p>Nós analisaremos e responderemos ao seu pedido em conformidade com a LGPD, dentro de prazos razoáveis.</p>
      <p><a href="/privacy">Voltar à Política de Privacidade</a></p>
    </body>
    </html>
    """
    return Response(html, status=200, mimetype="text/html")