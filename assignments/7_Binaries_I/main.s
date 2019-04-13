section .text

global main
main:
  push rbp
  mov rbp, rsp
  sub rsp, 0x10
  mov DWORD [rbp-0x8], 0x1ceb00da
  mov DWORD [rbp-0x4], 0xfeedface

  mov eax, DWORD [rbp-0x4]
  mov esi, eax
  mov edi, a_fmt  ; see data section at bottom
  mov eax, 0x0
  call printf

  mov eax, DWORD [rbp-0x8]
  mov esi, eax
  mov edi, b_fmt  ; see data section at bottom
  mov eax, 0x0
  call printf

  mov eax, DWORD [rbp-0x8]
  xor DWORD [rbp-0x4],eax
  mov eax, DWORD [rbp-0x4]
  xor DWORD [rbp-0x8],eax
  mov eax, DWORD [rbp-0x8]
  xor DWORD [rbp-0x4],eax

  mov eax, DWORD [rbp-0x4]
  mov esi, eax
  mov edi, a_fmt  ; see data section at bottom
  mov eax, 0x0
  call printf

  mov eax, DWORD [rbp-0x8]
  mov esi, eax
  mov edi, b_fmt  ; see data section at bottom
  mov eax, 0x0
  call printf

  mov eax, 0x0
  pop rbp
  ret
  nop

section .data
a_fmt:
  db 'a = %d\n', 0  ; null-terminated format string

                    ; db is an assembler directive that initializes a few bytes
                    ; of memory. dw, dd, and dq do this similarly with different
                    ; sizes of data.

b_fmt:
  db 'b = %d\n', 0  ; null-terminated format string
