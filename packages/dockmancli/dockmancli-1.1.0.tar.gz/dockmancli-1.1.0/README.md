# Docker Manager CLI

Manage Docker interactively from the terminal. You can create and delete images, containers, networks and volumes.
You can also create a yaml configuration file with which you can create one or more images, containers, networks and volumes.

### Changelog

1.1.0
- Containers
  - Improved log option

1.0.1
- Containers
  - New refresh option
  - New log option
- Images
  - New refresh option

1.0.0
Initial version

# Main menu

From the main menu you can access Containers, Images, Volumes and Networks. You can also create all this from a yaml file.

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//main_menu.png)

## Containers

From the menu you will be able to list or create containers

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/container_menu.png)

### Containers list

It will show all containers, and their status, in ascending order. The order can be changed in descending order. You can enable the auto-completion option, which will filter the containers as you type. Another option is to select multiple containers, for example, to delete them.

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/containers_list.png)

Container options:

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/container_options.png)

Descending order:

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/containers_list_desc.png)

Autocomplete:

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/containers_autocomplete.png)

Multiselect:

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/containers_multiselect.png)
![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/containers_multiselect_options.png)

### Container creation

A container can be created from an existing image, or through a yaml file. First, select the image

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/container_creation_from_image_1.png)
![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//containers/container_creation_from_image_2.png)

## Images

From the menu you will be able to list or create images

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//images/image_menu.png)

### Images list

Like the containers, the list of images can be sorted in ascending and descending order, enable auto-completion and select multiple images

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//images/images_list.png)

### Image creation

An image can be created by pull, Dockerfile or yaml file

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//images/image_creation_options.png)

#### Pull

Pull the image

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//images/image_pull.png)

#### Dockerfile

Select a Dockerfile from your computer

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//images/image_dockerfile.png)

## Volumes

From the menu you will be able to list or create volumes

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//volumes/volume_menu.png)

### Volumes list

It will show the list of volumes

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//volumes/volumes_list.png)

Volume options:

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//volumes/volume_options.png)

### Volume creation

A volume can be created manually or yaml file

#### Manually

Enter name and driver to create the volume

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//volumes/volume_creation_manually.png)

## Networks

From the menu you will be able to list or create networks

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//networks/network_menu.png)

### Networks list

Networks can be sorted in ascending and descending order, enable auto-completion and select multiple networks

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//networks/networks_list.png)

Network options:

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//networks/network_options.png)

### Network creation

A network can be created manually or yaml file

#### Manually

Enter name and driver to create the network

![](https://raw.githubusercontent.com/MDKPredator/dockmancli/main/images//networks/network_creation_manually.png)

## Yaml

A yaml file can be used to create containers, images, networks and volumes from the main menu, or from each of the options (containers, images, networks and volumes). An example of a file is:

```yaml
images:
  - image:
      path: /path/to/dockerfile/
      dockerfile: Dockerfile
      tag: image-test:1.0.0
      nocache: True
      forcerm: True
      pull: True

  - image:
      path: /path/to/another/dockerfile/
      dockerfile: Dockerfile-python
      tag: python-image-test:1.0.0
      nocache: True
      forcerm: True
      pull: True
#      container_limits:
#        memory: 1073741824

containers:
  - container:
      image: container-test:1.0.0
      name: image-test:1.0.0
      ports:
        # container:host
        80: 8080
      mem_limit: 100m
      network: net-test
      restart_policy:
        Name: always

networks:
  - network:
      name: net-test
      driver: bridge
  - network:
      name: net-test2
      driver: bridge
  - network:
      name: net-test3
      driver: bridge

volumes:
  - volume:
      name: volumeTest
      driver: local
```

### urllib3 warning
If you receive a warning like this:
> NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020

You should install OpenSSL 1.1.1 or higher. More info [here](https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu)
