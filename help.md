                          __         ____
    ____ ___  __  _______/ /_  ___  / / /
   / __  __ \/ / / / ___/ __ \/ _ \/ / / 
  / / / / / / /_/ (__  ) / / /  __/ / /  
 /_/ /_/ /_/\__, /____/_/ /_/\___/_/_/   
           /____/ Help center

Usage: msh <command>

<...> = required
[...] = optional

Commands:
  collection|c clone|c <url> [collection-name] - Clone a collection from a git repository
      url - The URL of the git repository to clone
      collection-name - The name of the collection to create. Default is the name of the repository

  collection|c list|ls - List all collections

  collection|c new|n <collection-name> - Create a new collection
      collection-name - The name of the collection to create

  edit|e [script-name] - Open a specified or all scripts in the editor
      script-name - If provided, the script with the specified name will be opened in the editor

  help|h - Get help for myshell

  list|ls [tag] [flags] - List all available commands
      tag - If provided, only scripts with the specified tag will be listed
      Flags:
          -group|-g - Group the scripts by collection

  migrate-scripts - Migrate all existing scripts to msh

  new|n <new-script> [collection-name] [flags]- Create a new script
      script-name - The name of the script to create
      collection-name - The name of the collection to add the script to. The default collection can be set in the config
      Flags:
          -edit|-e - Open the script in the editor after creation

  print|p <script-name> - Print the contents of a script
      script-name - The name of the script to print

  sync|s [collection-name] [flags] - Synchronize all or one collections
      collection-name - The name of the collection to synchronize
      Flags:
          -u|-up - Push changes to the remote repository
          -d|-detached - Synchronize the collection in detached mode

  version|v - Print the version of myshell

 Global flags (apply to all commands):
  --quiet|--q - Do not print any output
