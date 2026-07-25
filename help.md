```
myshell v1.3.0

New version available: 1.3.0 -> 1.2.1
Run 'msh-update' to update

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
  alias|a <script-name> <content> - Create a new alias for a command
      script-name - The name of the new script to create
      content - The content of the new script to create

  autocomplete <enable|disable|status|get> - Enable or disable autocomplete for the CLI (only works for bash)
      enable - Enable autocomplete for the CLI
      disable - Disable autocomplete for the CLI
      status - Show the current status of autocomplete
      get - Get autocomplete suggestions for the CLI

  collection|c clone|c <url> [collection-name] [flags] - Clone a collection from a git repository
      url - The URL of the git repository to clone
      collection-name - The name of the collection to create. Default is the name of the repository
      Flags:
		-print-path|-P - Print the path of the cloned collection

  collection|c list|ls [flags] - List all collections
      Flags:
		-raw|-r - Print raw output

  collection|c new|n <collection-name> - Create a new collection
      collection-name - The name of the collection to create
      Flags:
          -bin|-b - Create a bin directory within the collection

  copy|cp <original-script> <new-script> - Copy a script to a new file
      original-script - The script to copy
      new-script - The name of the new script file

  details|d <script> [flags] - Get more information about a script
      script - The name of the script to get details for
      Flags:
          -json - If specified, the output will be in JSON format

  docs [port] - Starts the docs server on the specified port (default: 8428).
      port - The port on which to start the docs server (default: 8428).

  edit|e [script-name] [flags] - Open a specified or all scripts in the editor
      script-name - If provided, the script with the specified name will be opened in the editor
      Flags:
          -quick|-q - Use the quick editor command

  generate-docs - Generate a documentation html file.

  help|h [command] - Get help for myshell
      command - The command to get help for

  list|ls [tag] [flags] - List all available commands
      tag - If provided, only scripts with the specified tag will be listed
      Flags:
          -collection|-c - Show the collection of the scripts
          -group|-g - Group the scripts by collection
          -simple|-s - Print the list in a simple format
          -time|-t - Print the time tag of the script
          -path|-p - Print the path of the script instead of the description
          -name|-n - Print only the name of the script

  manual|m <script> [flags] - Get the manual for the script
      script - The name of the script to get the manual for
      Flags:
          -print|-p - Print the content of the script before the manual
          -run|-r - Run the script after displaying the manual

  migrate-scripts - Migrate all existing scripts to msh

  move|mv <script> <dest-collection> - Move a script to a different collection
      script - The name of the script to move
      dest-collection - The name of the collection to move the script to

  new|n <new-script> [collection-name] [flags]- Create a new script
      script-name - The name of the script to create
      collection-name - The name of the collection to add the script to. The default collection can be set in the config
      Flags:
          -docs|-dc - Update the docs after creating the script
          -edit|-e - Open the script in the editor after creation
          -interactive|-it - Run the command in interactive mode, prompting for missing values (the name is not required in this mode)
          -man|-m - Add a manual to the script
          -local|-l - Create the script in the current directory
          -quick-edit|-qe - Open the script in the editor after creation, using the quick editor command
          -say-hello|-sh - Adds a line to the script that prints 'Hello from <script-name>!' when executed

  print|p <script-name> [flags] - Print the contents of a script
      script-name - The name of the script to print
      Flags:
          -run|-r - Run the script after printing

  remove|rm <script> [flags] - Remove a script
      script - The name of the script to remove
      Flags:
          -force|-f - Remove script without storing it in the trash

  restore <script> [collection-name] - Restore a script from the trash
      script - The name of the script to restore
      collection-name - The name of the collection to restore the script to

  run|r <script> [flags] - Run a script
      script - The name of the script to run
      Flags:
          -args|-a - Provide arguments for the script
          -extend|-x - Print the scripts commands while running
          -clear-log|-cl - Clear the command and run logs before running the script

  sync|s [collection-name] [flags] - Synchronize all or one collections
      collection-name - The name of the collection to synchronize
      Flags:
          -up|-u - Push changes to the remote repository
          -detached|-d - Synchronize the collection in detached mode

  version|v [flags] - Print the version of myshell
       Flags:
           -simple|-s - Print the version in a simple format

 Global flags (apply to all commands):
  --quiet|--q - Do not print any output

To get more information please visit: https://myshell.philipp-bonin.com/


```
