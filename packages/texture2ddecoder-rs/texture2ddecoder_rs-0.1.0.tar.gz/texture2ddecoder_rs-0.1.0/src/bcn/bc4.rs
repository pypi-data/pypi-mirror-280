use crate::bcn::bc3::decode_bc3_alpha;

#[inline]
pub fn decode_bc4_block(data: &[u8], outbuf: &mut [u32]) {
    decode_bc3_alpha(data, outbuf, 2);
}
