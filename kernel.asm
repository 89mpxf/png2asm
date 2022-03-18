; Initialize BIOS requirements
org 0x8000
bits 16

; Set video mode
mov ah, 0
mov al, 13h
int 0x10

; Load image data from disk
mov si, image
call display
jmp $

; Display image
display:
    pusha
    xor ax, ax
    lodsb
    mov cx, ax
    lodsb
    mov dx, ax
    .for_x:
        push dx
        .for_y:
            mov bh, 0
            lodsb
            mov ah, 0xC
            int 0x10
        sub dx, 1
        jnz .for_y
        pop dx
    sub cx, 1
    jnz .for_x
    popa
    ret

; Import image
image: incbin "image/image.bin"

; Assembler information
%assign usedMemory ($-$$)
%assign usableMemory (512*63)
%warning [usedMemory/usableMemory] Bytes used
times (512*63)-($-$$) db 0 
