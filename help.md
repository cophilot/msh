```
myshell v1.0.3

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
      Flags:
		-raw|-r - Print raw output
  collection|c new|n <collection-name> - Create a new collection
      collection-name - The name of the collection to create

  edit|e [script-name] [flags] - Open a specified or all scripts in the editor
      script-name - If provided, the script with the specified name will be opened in the editor
      Flags:
          -quick|-q - Use the quick editor command

  help|h - Get help for myshell

  list|ls [tag] [flags] - List all available commands
      tag - If provided, only scripts with the specified tag will be listed
      Flags:
          -collection|-c - Show the collection of the scripts
          -group|-g - Group the scripts by collection
          -simple|-s - Print the list in a simple format

  manual|m <script> - Get the manual for the script
      script - The name of the script to get the manual for

  migrate-scripts - Migrate all existing scripts to msh

  move|mv <script> <dest-collection> - Move a script to a different collection
      script - The name of the script to move
      dest-collection - The name of the collection to move the script to

  new|n <new-script> [collection-name] [flags]- Create a new script
      script-name - The name of the script to create
      collection-name - The name of the collection to add the script to. The default collection can be set in the config
      Flags:
          -edit|-e - Open the script in the editor after creation
          -man|-m - Add a manual to the script
          -local|-l - Create the script in the current directory
          -quick-edit|-qe - Open the script in the editor after creation, using the quick editor command

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
