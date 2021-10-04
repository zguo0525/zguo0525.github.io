# Yifan Yang's Personal Website

## References

Theme and customization based on https://github.com/pages-themes/minimal

Icons in author info section from https://fontawesome.com/v4.7/examples/

Repo organized as https://github.com/academicpages/academicpages.github.io

## Repo Structure

`_layouts` describes the (customized) layout of the HTML page  
`index.md` contains the main text  
`_config.yml` contains configuration parameters for the site  
`assets/fonts` contains all icons from font awesome  
`_sass` contains styling settings for font awesome, you need to change the `fa-font-path` in `_variables.scss` to the path where you store the icons  
`assets/css` imports the font awesome style to the site, then you can use the icon (examples in `_layouts`)