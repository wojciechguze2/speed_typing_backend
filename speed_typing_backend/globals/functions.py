def format_ms_to_string(time_ms: [float, int]):
    if not time_ms:
        return 0

    milliseconds = int(time_ms % 1000)
    seconds = int((time_ms // 1000) % 60)
    minutes = int(time_ms // 1000 // 60)

    return f"{minutes}m {seconds}s {milliseconds}ms"
