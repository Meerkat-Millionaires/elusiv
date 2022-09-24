use std::fmt;
use solana_program::program_error::ProgramError;

#[derive(Copy, Clone, Debug)]
pub enum ElusivWardenNetworkError {
    InvalidSignature,
    WardenRegistrationError,
}

impl From<ElusivWardenNetworkError> for ProgramError {
    fn from(e: ElusivWardenNetworkError) -> Self {
        ProgramError::Custom(e as u32)
    }
}

impl fmt::Display for ElusivWardenNetworkError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", *self as u32)
    }
}