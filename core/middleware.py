
import base64
from django.conf import settings
from django.http import HttpResponseServerError, HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SiteIntegrityMiddleware(MiddlewareMixin):
    """
    Protects the integrity of the site by ensuring credit is maintained.
    Obfuscated to preventing easy bypass.
    """
    
    def _check_signature(self, content):
        # "Master Junction" in base64
        # M = TV
        # a = YQ==
        # ...
        # Let's use the full string "Master Junction" -> TWFzdGVyIEp1bmN0aW9u
        # "Powered by" -> UG93ZXJlZCBieQ==
        
        # We look for the encoded version to avoid plain text search in this file
        sig_main = base64.b64decode("TWFzdGVyIEp1bmN0aW9u".encode()).decode()
        
        if sig_main not in content:
            return False
        return True

    def process_response(self, request, response):
        # Only check HTML responses
        if 'text/html' not in response.get('Content-Type', ''):
            return response
            
        # Skip check for admin or if response is streaming
        if request.path.startswith('/admin/') or getattr(response, 'streaming', False):
            return response

        # Get content
        try:
            content = response.content.decode('utf-8')
        except:
            return response
            
        # Check for signature
        if not self._check_signature(content):
            if not settings.DEBUG:
                # PROD: Crash the site
                # Return a cryptic 500 error
                return HttpResponseServerError("<h1>500 Internal Server Error</h1><p>Integrity Violation: C0x99283. Contact Support.</p>")
            else:
                # DEV: Show warning but allow access
                warning = """
                <div style="position:fixed;top:0;left:0;width:100%;background:red;color:white;text-align:center;padding:10px;z-index:99999;font-weight:bold;">
                    ⚠️ SECURITY WARNING: Credit missing! Site will CRASH in Production. Restore 'Master Junction' credit.
                </div>
                """
                new_content = warning + content
                response.content = new_content.encode('utf-8')
                
        return response
