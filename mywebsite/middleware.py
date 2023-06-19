from django.conf import settings
from django.contrib import auth
from django.contrib.sessions.middleware import SessionMiddleware
from django.utils import timezone

class SessionIdleTimeoutMiddleware(SessionMiddleware):
    def process_request(self, request):
        super().process_request(request)

        # Cek apakah pengguna sudah otentikasi
        if request.user.is_authenticated:
            # Periksa apakah ada timestamp idle session sebelumnya di session pengguna
            last_activity = request.session.get('last_activity')

            # Jika tidak ada, atur last_activity ke waktu sekarang
            if not last_activity:
                request.session['last_activity'] = timezone.now().timestamp()
            else:
                # Jika ada, cek waktu idle pengguna
                idle_duration = timezone.now().timestamp() - last_activity

                # Jika waktu idle melebihi batas yang ditentukan (dalam detik), logout pengguna
                if idle_duration > settings.SESSION_COOKIE_AGE:
                    auth.logout(request)

        # Update last_activity dengan waktu sekarang
        request.session['last_activity'] = timezone.now().timestamp()