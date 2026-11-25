#!/usr/bin/env python3
"""Scramble the defense page's text with the page password.

The readable text lives in _drafts/phd-defense/content.html, which is never committed (_drafts/ is in .gitignore).
This script packs it, encrypts it with the password, and writes the result into phd-defense/index.html as the
LOCKED string. Only that scrambled string is ever committed; the page unscrambles it in the visitor's browser.

    python3 _scripts/lock_defense.py            # asks for the password (twice)

Run it again after every edit to content.html, and commit phd-defense/index.html. Changing the password is the
same: run it with the new one. (Old versions of the page stay in git history, unlockable with the old password.)

How: PBKDF2-SHA256 (600,000 rounds) turns the password into two keys; the packed text is encrypted with AES-256-CTR
(via the macOS `openssl` command) and sealed with HMAC-SHA256, so a wrong password is always rejected.
Uses only Python's standard library and openssl.
"""
import base64, getpass, hashlib, hmac, os, re, subprocess, sys, zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, '_drafts', 'phd-defense', 'content.html')
PAGE = os.path.join(ROOT, 'phd-defense', 'index.html')
ROUNDS = 600_000   # must match the page script


def b64(b):
    return base64.b64encode(b).decode()


def aes_ctr(key, iv, data, decrypt=False):
    cmd = ['openssl', 'enc', '-aes-256-ctr', '-K', key.hex(), '-iv', iv.hex(), '-nosalt'] + (['-d'] if decrypt else [])
    return subprocess.run(cmd, input=data, capture_output=True, check=True).stdout


def main():
    text = open(SOURCE, encoding='utf-8').read()
    text = re.sub(r'\A\s*<!-- PRIVATE:.*?-->\s*', '', text, flags=re.S)   # the note at the top stays out

    password = os.environ.get('DEFENSE_PASSWORD')
    if not password:
        password = getpass.getpass('Page password: ')
        if getpass.getpass('Again: ') != password:
            sys.exit('The two passwords differ; nothing was changed.')
    if not password:
        sys.exit('Empty password; nothing was changed.')

    packer = zlib.compressobj(9, zlib.DEFLATED, -15)   # raw deflate, which the browser unpacks natively
    packed = packer.compress(text.encode('utf-8')) + packer.flush()

    salt = os.urandom(16)
    iv = os.urandom(8) + bytes(8)   # 8 random bytes, then a counter from zero (so the browser counts the same way)
    keys = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, ROUNDS, dklen=64)
    enc_key, mac_key = keys[:32], keys[32:]
    data = aes_ctr(enc_key, iv, packed)
    tag = hmac.new(mac_key, iv + data, hashlib.sha256).digest()
    assert zlib.decompress(aes_ctr(enc_key, iv, data, decrypt=True), -15).decode('utf-8') == text   # round trip

    page = open(PAGE, encoding='utf-8').read()
    locked = '.'.join(map(b64, (salt, iv, data, tag)))
    page, n = re.subn(r"const LOCKED = '[^']*';", f"const LOCKED = '{locked}';", page)
    if n != 1:
        sys.exit("Could not find the LOCKED line in phd-defense/index.html; nothing was changed.")
    open(PAGE, 'w', encoding='utf-8').write(page)
    print(f'Locked {len(text):,} characters into phd-defense/index.html. Commit that file (never the _drafts/ one).')


if __name__ == '__main__':
    main()
