from zdrive import Downloader

d = Downloader()
folder_id = '1dN0FsnGGx2ugH1Jzh1Q'  # replace string here with the folder id 
                                    # for the data folder shared to everyone


if __name__ == '__main__':
     d.downloadFolder(folder_id)