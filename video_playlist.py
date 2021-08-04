"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""
    __PlayListItems = []
    __PlayListName = ""
    def __init__(self , playlist_name):
        self.__PlayListName = playlist_name

    def get_playlist_name(self):
        return self.__PlayListName
    
    def add_item_in_playlist(self , videoInfo):
        if videoInfo in self.__PlayListItems:
            print("Cannot add video to " + self.__PlayListName + ": Video already added")
        else:
            self.__PlayListItems.append(videoInfo)
            print("Added video to " + self.__PlayListName + ": " + videoInfo.title)
    
    def remove_item_in_playlist(self , videoInfo):
        if videoInfo in self.__PlayListItems:
            print("Removed video from " + self.__PlayListName + ": " + videoInfo.title)
            self.__PlayListItems.remove(videoInfo)
        else:
            print("Cannot remove video from " + self.__PlayListName + ": Video already added")
    
    def clear_items_in_playlist(self):
        for all_items in self.__PlayListItems:
            self.__PlayListItems.remove(all_items)
            
    def display_playlist(self):
        if (self.__PlayListItems):
            for each_item in self.__PlayListItems:
                tag = str(each_item.tags)[1:-1].replace(",","").replace("'","")
                print(each_item.title + " (" + each_item.video_id + ")" + " [" + tag + "]")
        else:
            print("No videos here yet")