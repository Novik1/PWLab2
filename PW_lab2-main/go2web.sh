#! /usr/bin/env bash

# ADD YOUR CODE HERE

#chmod u+x HandleUrl.py
#chmod u+x python3

function url_func() {
    py - <<END
import HandleUrl
HandleUrl.handle_url("$url")
END
}

function term_func(){
  py - <<END
import HandleUrl
HandleUrl.search_term("$url")
END
}

function save_func(){
  py - <<END
import HandleUrl
HandleUrl.save_page("$url")
END
}

Help()
{
   # Display Help
   echo
   echo "Syntax: scriptTemplate [-u|s|h|p]"
   echo "options:"
   echo "go2web.sh -u <URL>         # make an HTTP request to URL and print the response"
   echo "go2web.sh -s <search-term> # search the term using your favorite search engine and print top 10 results"
   echo "go2web.sh -p <URL>         # saves the web-page"
   echo "go2web.sh -h               # show help"
   echo
}

#GetUrl($command)
#{
#
#}

command="<URL>"
term="<search-term>"

while getopts ":hu:s:p:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      u)# scan url
        url=$OPTARG
#        python3 -c "import HandleUrl; HandleUrl.handle_url($url)";;
#        echo $(python HandleUrl.py $url) > /dev/null
#        tr ' ' '\n' < "$(url_func "$url")"
#        url_func "$url"
#        answer="$(url_func "$url")"
#        echo "$answer"
#        echo "$(echo -e "$(url_func "$url")")"
#        echo "$processed_answer"
        url_func "$url"
        ;;
      s)
        term=$OPTARG
        yahoo="https://search.yahoo.com/search?p="
        url=$yahoo$term
        echo "$url"
        term_func "$url"
        ;;
      p)
        page=$OPTARG
        save_func "$url"
        ;;
      \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done


