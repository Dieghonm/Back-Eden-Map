# app/services/email_service.py
import os
from typing import Optional

def send_recovery_code_email(to_email: str, user_login: str, recovery_code: str) -> bool:
    """
    Envia email com código de recuperação de senha
    
    Args:
        to_email: Email de destino
        user_login: Login do usuário
        recovery_code: Código de 4 dígitos
    
    Returns:
        bool: True se enviado com sucesso, False caso contrário
    """
    
    # Template do email
    subject = "Eden Map - Password Recovery Code"
    
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .content {{
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .code {{
                font-size: 32px;
                font-weight: bold;
                color: #4CAF50;
                text-align: center;
                padding: 20px;
                margin: 20px 0;
                background-color: #f9f9f9;
                border-radius: 5px;
                letter-spacing: 8px;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                font-size: 12px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="content">
                <h2>Password Recovery</h2>
                <p>Hello <strong>{user_login}</strong>,</p>
                <p>You requested a password recovery for your Eden Map account.</p>
                <p>Use the code below to reset your password:</p>
                
                <div class="code">{recovery_code}</div>
                
                <p>This code will expire in <strong>15 minutes</strong>.</p>
                <p>If you didn't request this code, please ignore this email.</p>
                
                <div class="footer">
                    <p>Eden Map Team</p>
                    <p>This is an automated email, please do not reply.</p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    text_body = f"""
    Eden Map - Password Recovery
    
    Hello {user_login},
    
    You requested a password recovery for your Eden Map account.
    
    Your recovery code is: {recovery_code}
    
    This code will expire in 15 minutes.
    
    If you didn't request this code, please ignore this email.
    
    Eden Map Team
    """
    
    try:
        # TODO: Integrar com serviço de email real (Brevo, SendGrid, etc)
        # Por enquanto, apenas simular envio
        
        print("\n" + "="*60)
        print("📧 EMAIL SENT (SIMULATED)")
        print("="*60)
        print(f"To: {to_email}")
        print(f"Subject: {subject}")
        print(f"Recovery Code: {recovery_code}")
        print("="*60 + "\n")
        
        # Quando integrar com serviço real, descomentar código abaixo:
        """
        import requests
        
        # Exemplo com Brevo (antigo SendinBlue)
        BREVO_API_KEY = os.getenv("BREVO_API_KEY")
        
        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "api-key": BREVO_API_KEY,
                "Content-Type": "application/json"
            },
            json={
                "sender": {
                    "name": "Eden Map",
                    "email": "noreply@edenmap.com"
                },
                "to": [{"email": to_email}],
                "subject": subject,
                "htmlContent": html_body,
                "textContent": text_body
            }
        )
        
        return response.status_code == 201
        """
        
        return True
        
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False