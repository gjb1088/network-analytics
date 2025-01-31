# Example base image for AWX Execution Environments
FROM quay.io/ansible/awx-ee:latest

# Switch to root to install packages
USER 0

# Install required dependencies
RUN dnf install -y iputils wget dejavu-sans-fonts fontconfig && dnf clean all

# Manually download Noto Color Emoji font
RUN wget https://github.com/googlefonts/noto-emoji/raw/main/fonts/NotoColorEmoji.ttf -O /usr/share/fonts/NotoColorEmoji.ttf

# Rebuild the font cache
RUN fc-cache -fv

# Install required Python libraries
RUN python3 -m ensurepip --upgrade && \
    python3 -m pip install --no-cache-dir --upgrade pip setuptools wheel && \
    python3 -m pip install --no-cache-dir matplotlib fpdf2
    
# Copy emoji PNGs into the image
COPY satellite_antenna.png /usr/local/bin/latency_icon.png
COPY zap.png /usr/local/bin/speed_icon.png
COPY alarm_clock.png /usr/local/bin/uptime_icon.png

# Copy Python scripts into the image
COPY generate_graphs.py /usr/local/bin/generate_graphs.py
COPY generate_pdf_report.py /usr/local/bin/generate_pdf_report.py

# Set permissions
RUN chmod +x /usr/local/bin/generate_graphs.py /usr/local/bin/generate_pdf_report.py

# Switch back to the non-root user used by the AWX EE
USER 1001
