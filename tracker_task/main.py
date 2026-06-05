from task import add, update, delete, mark_in_progress, mark_done, lista
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI simples de tarefas")
    subparser = parser.add_subparsers(dest="comando", required=True)

    #add
    p_add = subparser.add_parser("add")
    p_add.add_argument("descricao", type=str)

    #update
    p_update = subparser.add_parser("update")
    p_update.add_argument("id", type=int)
    p_update.add_argument("descricao", type=str)

    #delete
    p_delete = subparser.add_parser("delete")
    p_delete.add_argument("id", type=int)

    #mark-in-progress
    p_progress = subparser.add_parser("mark-in-progress")
    p_progress.add_argument("id", type=int)

    #done
    p_done = subparser.add_parser("mark-done")
    p_done.add_argument("id", type=int)

    #list
    p_list = subparser.add_parser("list")
    p_list.add_argument("status", nargs="?", choices=["done", "in-progress", "todo"])

    args = parser.parse_args()
    if args.comando == "add":
        add(args.descricao)
    elif args.comando == "update":
        update(args.id, args.descricao)
    elif args.comando == "delete":
        delete(args.id)
    elif args.comando == "mark-in-progress":
        mark_in_progress(args.id)
    elif args.comando == "mark-done":
        mark_done(args.id)
    elif args.comando == "list":
        lista(args.status)

if __name__ == "__main__":
    main()