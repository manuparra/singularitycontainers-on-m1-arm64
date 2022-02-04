# Singularity Containers on M1

This is a repository containing a ready-to-use environment for singularity in arm64 (M1). It has been prepared specifically for the [SKA SRC  training on containers  event](https://gitlab.com/ska-telescope/src/ska-src-training-containers) and allows you the use of [singularity containers](https://sylabs.io/singularity) with Apple's M1 architecture. 

## Install UTM for Apple M1

Click here: [UTM for M1](https://mac.getutm.app/)

Download it and then install it.

## Download and unzip the pre-build UTM image ready to use.

Click here to [download this image](https://drive.google.com/file/d/1STHZq81HIRFit2en5jzAPaHSLfPc7tVB/view?usp=sharing).

This is an image created using Ubuntu 20.04 for ARM 64 Architecture.

After that, unzip the file downloaded (from 3GB to 6GB).

# Import UTM image from the UTM application

Open UTM application, then click on the menu "File" and then "Import", select the image `skatraining-singularity.utm`.

![Import image](./media/importimage.png)

# Start the image

Click on the recently imported image and then click `>` to start.

After that you will see login screen. 

Use the following credentials:

- username: **ska**
- passwoord: **ska**


# Connect to the environmente using SSH.

Connecting via SSH is a better option than directly using the shell that appears from the screen when starting the Virtual Machine. 

To do that, open a Terminal in your host system and type the following:

```
ssh -p 22022 ska@localhost
```

and you have to use the following credentials:

- username: **ska**
- passwoord: **ska**


# Change keyboard layout

Because the image was built on my machine, in the installation I used my local keyboard layout, so to use your own keyboard layout (FR, DE, UK, ...), to do it you can type the following:

```
sudo dpkg-reconfigure keyboard-configuration
```

And then select your keyboard layout. Then you have to reboot the virtual machine by typing: ``sudo reboot``



# Acknowledgments

Mateusz Malenta and Alex Clarke
