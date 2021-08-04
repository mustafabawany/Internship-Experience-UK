"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    
    __video_count = 0
    __video_info = ""
    __video_paused = 0
    __allPlayLists = []

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos: ")
        all_videos = self._video_library.get_all_videos()
        all_videos.sort()

        for i in all_videos:
            video_object= self._video_library.get_video(i)
            tag = str(video_object.tags)[1:-1].replace(",","").replace("'","")
            print(video_object.title + " (" + video_object.video_id + ")" + " [" + tag + "]")
        
    def play_video(self, video_id):

        """Plays the respective video.
        
        Args:
            video_id: The video_id to be played.
        """
        self.__video_paused = 0

        if self.__video_count == 1:
            if self._video_library.get_video(video_id) != None:
                self.stop_video()
        
        self.__video_info = self._video_library.get_video(video_id)
        
        if self.__video_info == None:
            print("Cannot play video: Video does not exist")

        else:
            self.__video_count = 1
            
            print("Playing video:", self.__video_info.title)
        
    def stop_video(self):
        """Stops the current video."""

        if self.__video_info == "":
            print("Cannot stop video: No video is currently playing")
            
        elif self.__video_info != None:
            print("Stopping video:" , self.__video_info.title)
            self.__video_info = ""
            self.__video_count = 0    
            
    def play_random_video(self):
        """Plays a random video from the video library."""
        
        all_videos = self._video_library.get_all_videos()
        random_video = random.choice(all_videos)
        self.play_video(random_video) 
        
    def pause_video(self):
        """Pauses the current video."""

        if  self.__video_info == "":
            print("Cannot pause video: No video is currently playing")

        elif self.__video_info != None:
            if self.__video_paused == 0:
                print("Pausing video:" , self.__video_info.title)
                self.__video_paused = 1
            else:
                print("Video already paused:" , self.__video_info.title)

    def continue_video(self):
        """Resumes playing the current video."""

        if self.__video_info == "":
            print("Cannot continue video: No video is currently playing")

        elif self.__video_info != None:
            if self.__video_paused == 0:
                print("Cannot continue video: Video is not paused")
            else:
                print("Continuing video:" , self.__video_info.title)
                self.__video_paused = 0

    def show_playing(self):
        """Displays video currently playing."""

        if self.__video_info == "":
            print("No video is currently playing")

        elif self.__video_info != None:
            tag = str(self.__video_info.tags)[1:-1].replace(",","").replace("'","")
            if self.__video_paused == 0:
                print("Currently playing: " + self.__video_info.title + " (" + self.__video_info.video_id  + ")" + " [" + tag + "]")
            else:
                print("Currently playing: " + self.__video_info.title + " (" + self.__video_info.video_id  + ")" + " [" + tag + "] - PAUSED")
            
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        for p in self.__allPlayLists:
            temp = p.get_playlist_name()
            if  temp.casefold() == playlist_name.casefold():
                print("Cannot create playlist: A playlist with the same name already exists")
                return
        current_playlist = Playlist(playlist_name)
        self.__allPlayLists.append(current_playlist)
        print("Successfully created new playlist: " + playlist_name)
        
    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        
        """Video is valid"""
            
        for p in self.__allPlayLists:
            temp = p.get_playlist_name()
            if temp.casefold() == playlist_name.casefold():
                video = self._video_library.get_video(video_id)
                if video != None:
                    """Found perticular Playlist"""
                    p.add_item_in_playlist(video)
                    return
                else:
                    print("Cannot add video to " + playlist_name + ": Video does not exist")
                    return
        
        print("Cannot add video to " + playlist_name +  ": Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""
        
        if len(self.__allPlayLists):
            print("Showing all playlists:")
            for each_playlist in self.__allPlayLists:
                print(each_playlist.get_playlist_name())
        else:
            print("No playlists exist yet")   

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for p in self.__allPlayLists:
            temp = p.get_playlist_name()
            if temp.casefold() == playlist_name.casefold():
                """Found perticular Playlist"""
                print("Showing playlist: " + playlist_name)
                p.display_playlist()  
                return
        print("Cannot show playlist " + playlist_name +  ": Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        for p in self.__allPlayLists:
            temp = p.get_playlist_name()
            if temp.casefold() == playlist_name.casefold():
                video = self._video_library.get_video(video_id)
                if video != None:
                    """Found perticular Playlist"""
                    p.remove_item_in_playlist(video)
                    return
                else:
                    print("Cannot remove video from " + playlist_name + ": Video does not exist")
                    return
        
        print("Cannot remove video from " + playlist_name +  ": Playlist does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for p in self.__allPlayLists:
            temp = p.get_playlist_name()
            if temp.casefold() == playlist_name.casefold():
                p.clear_items_in_playlist()
                print("Successfully removed all videos from " + playlist_name)
                return 

        print("Cannot clear playlist " + playlist_name +  ": Playlist does not exist")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for p in self.__allPlayLists:
            temp = p.get_playlist_name()
            if temp.casefold() == playlist_name.casefold():
                self.__allPlayLists.remove(p)
                print("Deleted playlist " + playlist_name)
                return 

        print("Cannot delete playlist " + playlist_name +  ": Playlist does not exist")
        
    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        all_videos.sort()
        tempList = dict()
        Flag = 0
        Count = "1"
        for i in all_videos:
            video_object= self._video_library.get_video(i)
            if search_term.casefold() in video_object.title.casefold():
                if Count == "1":
                    print("Here are the results for " + search_term + ":")
                Flag = Flag + 1
                tempList.update({Count: video_object})
                tag = str(video_object.tags)[1:-1].replace(",","").replace("'","")
                print(Count + ") " + video_object.title + " (" + video_object.video_id + ")" + " [" + tag + "]")
                Count = int(Count)
                Count = Count + 1
                Count = str(Count)
        
        if Flag == 0:
            print("No search results for " + search_term)
            return
        
        print ("Would you like to play any of the above? If yes, specify the number of the video. \nIf your answer is not a valid number, we will assume it's a no.")
        Choice = input()
        for i,j in tempList.items():
            a  = str(i)
            if a == Choice:
                Choice = int (Choice)
                self.play_video(j.video_id)
                return
            
    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos = self._video_library.get_all_videos()
        all_videos.sort()
        tempList = dict()
        Flag = 0
        Count = "1"
        
        for i in all_videos:
            video_object= self._video_library.get_video(i)
            tag = str(video_object.tags)[1:-1].replace(",","").replace("'","")
            # print(tag)
            if video_tag in video_object.tags:
                Flag = Flag + 1
                if Count == "1":
                    print("Here are the results for " + video_tag + ":")
                # tempList.append(video_object)
                tempList.update({Count: video_object})
                tag = str(video_object.tags)[1:-1].replace(",","").replace("'","")
                print(Count + ") " + video_object.title + " (" + video_object.video_id + ")" + " [" + tag + "]")
                Count = int(Count)
                Count = Count + 1
                Count = str(Count)
        
        if Flag == 0:
            print("No search results for " + video_tag)
            return
        
        print ("Would you like to play any of the above? If yes, specify the number of the video. \nIf your answer is not a valid number, we will assume it's a no.")
        Choice = input()
        for i,j in tempList.items():
            a  = str(i)
            if a == Choice:
                Choice = int (Choice)
                self.play_video(j.video_id)
                return

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
