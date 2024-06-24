import argparse

import uvicorn


def start(env_mode: str = "dev", host: str = "127.0.0.1", port: int = 8000) -> None:
    """Start the server."""
    dev_mode = True if env_mode == "dev" else False

    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=dev_mode,
        reload_includes="*",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start the server.")
    parser.add_argument(
        "-e", "--env", type=str, default="dev", choices=["dev", "prod"], required=True
    )
    parser.add_argument("-ht", "--host", type=str, default="127.0.0.1", required=False)
    parser.add_argument("-pt", "--port", type=int, default=8000, required=False)

    args = parser.parse_args()
    start(args.env, args.host, args.port)
