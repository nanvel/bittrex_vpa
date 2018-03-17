import asyncio
import sys


if __name__ == '__main__':
    _, command, *arguments = sys.argv

    ioloop = asyncio.get_event_loop()

    if command == 'watch':
        from vpa.watcher import main
        ioloop.run_until_complete(main(market=arguments[0]))

    elif command == 'server':
        from vpa.server import main
        main()

    else:
        raise ValueError("Unknown command.")
