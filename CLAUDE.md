# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Quarto-based blog/experiment site for Hariom Narang. The site is published at https://pages.narang99.in and focuses on finished/archived experiments and projects.  

## Common Commands

### Building and Previewing
- `quarto render` - Build the entire site to the `_site/` directory
- `quarto preview` - Start development server with live reload
- `quarto render [filename]` - Render a specific file (e.g., `quarto render posts/how-long-do-i-descend.ipynb`)

### Site Management
- `quarto publish` - Publish the site (configured for GitHub Pages via CNAME)

## Architecture

### Content Structure
- **Root**: Contains main site files (`index.qmd`, `about.qmd`)
- **`posts/`**: Blog posts and experiments
  - `_metadata.yml`: Default settings for all posts (freeze: true, title-block-banner: true)
  - Individual post files (`.qmd`, `.ipynb`)

### Configuration
- **`_quarto.yml`**: Main site configuration
  - Site title: "Hariom Narang's Pages"
  - Theme: Custom Gruvbox Material (light/dark variants)
  - Syntax highlighting: Gruvbox variants
  - MathJax enabled for mathematical content
  - Bootstrap-based layout with GitHub integration

### Styling
- **`gruvbox-material-light.scss`**: Light theme customizations
- **`gruvbox-material-dark.scss`**: Dark theme customizations (currently modified)
- **`ft.scss`**: Additional styling file

### Key Features
- Responsive design with full-page layout
- RSS feed generation
- Automatic post listing with thumbnails
- Mathematical content support via MathJax
- Jupyter notebook integration
- GitHub integration in navigation

## Development Notes

### Content Creation
- Posts support both Quarto Markdown (`.qmd`) and Jupyter notebooks (`.ipynb`)
- All posts have `freeze: true` by default to cache computational output
- New posts should be added to the `posts/` directory
- Mathematical content is well-supported with MathJax

### Theme Customization
The site uses a custom Gruvbox Material theme with light/dark mode support. Theme files are SCSS-based and compile during the Quarto build process.

### Site Deployment
The site is configured for GitHub Pages deployment with a custom domain (experiments.narang99.in) specified in the CNAME file.