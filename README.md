# CioBot - Bot de Voz Premium con ElevenLabs

**CioBot** es un bot de Discord avanzado que utiliza la tecnología de IA de **ElevenLabs** para proporcionar una experiencia de Texto a Voz (TTS) extremadamente realista y personalizada.

## Características

- **Voces de Alta Fidelidad**: Integración directa con la API de ElevenLabs (modelo `eleven_multilingual_v2`).
- **Perfiles Personalizados**: Soporte para múltiples voces preconfiguradas (Cio, Yahir, Lloron, Checho).
- **Interacción Fluida**: El bot se une automáticamente a tu canal de voz cuando le pides que hable.
- **Gestión de Sesión**: Comandos simples para cambiar de voz o desconectar al bot.

## Comandos Principales

- `!habla [texto]`: El bot genera el audio del texto con la voz activa y lo reproduce en tu canal de voz.
- `!voces`: Muestra la lista de voces disponibles configuradas en el sistema.
- `!cambiarvoz [nombre]`: Cambia la voz actual por una de las disponibles (ej. `!cambiarvoz yahir`).
- `!vete`: Desconecta al bot del canal de voz actual.

## Requisitos Técnicos

- **Python 3.10+**
- **FFmpeg**: Necesario para que Discord pueda procesar y reproducir los archivos de audio.
- **API Key de ElevenLabs**: Una cuenta activa con créditos disponibles.

## Configuración (Archivo .env)

Para que el bot funcione, debes configurar las siguientes variables en un archivo `.env` en la raíz:

```env
DISCORD_TOKEN=tu_token_de_discord
ELEVENLABS_API_KEY=tu_api_key_de_elevenlabs
VOICECIO_ID=id_de_voz_cio
VOICEYAHIR_ID=id_de_voz_yahir
VOICELLORON_ID=id_de_voz_lloron
VOICECHECHO_ID=id_de_voz_checho
```

## Instalación

1.  Clona el repositorio.
2.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3.  Asegúrate de tener **FFmpeg** instalado y accesible en tu PATH.
4.  Ejecuta el bot:
    ```bash
    python bot_voz.py
    ```

## Notas de Uso
El bot genera archivos temporales `audio_eleven.mp3` que se eliminan automáticamente tras cada reproducción para mantener limpio el almacenamiento.

## Licencia
Este proyecto está bajo la licencia MIT.
