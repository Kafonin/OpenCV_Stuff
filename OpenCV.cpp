#include <opencv2/core.hpp>
#include "opencv2/opencv.hpp"
#include <opencv2/imgcodecs.hpp>
#include <iostream>


using namespace std;
using namespace cv;


int main(int, char**)
{
	Mat src;

	VideoCapture cap(0);  // Create a VideoCapture object and open the input file. If the input is the web camera, pass 0 instead of the video file name

	//Check if camera opened sauccessfully
	if (!cap.isOpened())
	{
		cout << "Error opening video stream or file" << endl;
		return -1;
	}

	//Get one frame from camera to know frame size and type
	cap >> src;
	//Check if we succeeded
	if (src.empty())
	{
		cerr << "ERROR! Blank frame grabbed.\n";
		return -1;
	}
	bool isColor = (src.type() == CV_8UC3);

	//INITIALIZE VIDEO WRITER
	VideoWriter writer;
	int codec = VideoWriter::fourcc('M', 'J', 'P', 'G'); //Select desired codec (must be available at runtime)
	double fps = 25.0;
	string filename = "./live.avi";
	writer.open(filename, codec, fps, src.size(), isColor);

	//check if we succeeded
	if (!writer.isOpened())
	{
		cerr << "Could not open the output video file for write\n";
		return -1;
	}

	//GRAB AND WRITE LOOP
	cout << "Writing videofile: " << filename << endl
		<< "Press any key to terminate" << endl;

	for (;;)
	{
		//check if we succeeded
		if (!cap.read(src))
		{
			cerr << "ERROR! Blank frame grabbed.\n";
			break;
		}
		//encode the frame into the video file stream
		writer.write(src);
		//show live and wait for a key with timeout long enough to show images
		imshow("Live", src);
		if (waitKey(5) >= 0)
		{
			break;
		}
	}
	//the video file will be closed and released automatically in videowriter destructor	
	return 0;
}